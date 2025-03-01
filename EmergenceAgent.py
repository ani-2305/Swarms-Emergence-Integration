import os
import time
import uuid
import requests
from dotenv import load_dotenv
from pathlib import Path

from swarm import Agent

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def call_emergence(prompt: str) -> str:
    """
    Calls Emergence AI's orchestrator with a prompt,
    then polls until success or fail/time out.
    Returns the final text from Emergence.
    """
    api_key = os.environ.get("EMERGENCE_API_KEY")
    if not api_key:
        return "No Emergence API Key configured. Please set EMERGENCE_API_KEY."

    base_url = "https://api.emergence.ai/v0/orchestrators/em-orchestrator/workflows"
    headers = {
        "apikey": api_key,
        "Content-Type": "application/json",
        "Client-ID": str(uuid.uuid4())
    }

    # Step A: Create the workflow
    try:
        create_resp = requests.post(base_url, headers=headers, json={"prompt": prompt}, timeout=30)
        create_resp.raise_for_status()
        workflow_id = create_resp.json()["workflowId"]
        print(f"[Emergence Agent] Created workflow: {workflow_id}")
    except Exception as e:
        return f"Error creating Emergence workflow: {str(e)}"

    # Step B: Poll until success/fail
    poll_url = f"{base_url}/{workflow_id}"
    poll_count = 1

    while True:
        print(f"[Emergence Agent] Polling attempt {poll_count}...")
        poll_count += 1
        time.sleep(15)  # Wait 15s between polls

        try:
            poll_resp = requests.get(poll_url, headers=headers, timeout=30)
            poll_resp.raise_for_status()
            response_json = poll_resp.json()
            data_obj = response_json.get("data", {})
            status = data_obj.get("status", "UNKNOWN")

            if status == "SUCCESS":
                return data_obj.get("output", "No output provided by Emergence.")
            elif status in ("FAILED", "TIMEOUT"):
                return f"Workflow ended with status {status}"
        except Exception as e:
            return f"Polling error: {str(e)}"

# Now define an Agent with a function
def emergence_function(prompt: str) -> str:
    """
    A function that can be called by the Swarm agent to run Emergence.
    """
    return call_emergence(prompt)

# Finally, create a Swarm agent
EmergenceAgent = Agent(
    name="EmergenceAgent",
    description="""
You are Emergence Agent. You have access to an 'emergence_function' that can call Emergence AI's Web Orchestrator.
If the user asks any question or wants any web-related automation, you MUST call 'emergence_function' with the prompt.
""",
    # The functions this agent can call:
    functions=[emergence_function],
    model="gpt-4o"
)
