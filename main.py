# main.py
from swarm import Swarm
from EmergenceAgent import EmergenceAgent

def main():
    client = Swarm()

    user_message = input("Enter your prompt: ")

    print("\nRunning conversation with EmergenceAgent...\n")

    # We pass a single user message
    response = client.run(
        agent=EmergenceAgent,
        messages=[{"role": "user", "content": user_message}],
        # optional context variables if you want
        context_variables={},
        max_turns=5,
        debug=True  # show debug logs
    )

    # The final response includes updated messages
    final_msg = response.output if response.success else response.error
    print("\n=== Final EmergenceAgent Response ===")
    print(final_msg)

if __name__ == "__main__":
    main()
