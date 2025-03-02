# Swarms and Emergence AI Web Orchestrator Integration

This repository demonstrates how to integrate [Swarms](https://github.com/kyegomez/swarms) with [Emergence AI's Web Orchestrator](https://api.emergence.ai/). It uses **Swarms** for agent-based automation and **Emergence AI** for web automation workflows.

---

## Project Overview

- **`EmergenceAgent.py`**: Main Python file that:
  1. Loads your API key from a `.env` file.
  2. Defines a function to create and poll an Emergence AI web workflow.
  3. Creates a Swarms Agent that can use the Emergence function.
  4. Handles the communication between Swarms and Emergence AI.

- **`main.py`**: Entry point that:
  1. Creates a Swarm client.
  2. Takes user input.
  3. Runs the EmergenceAgent with the input.
  4. Returns the final response.

- **`swarm/`**: Local module containing:
  - Base `Agent` class
  - `Swarm` orchestrator
  - `Result` data structure

- **`.env`**: File containing your `EMERGENCE_API_KEY`. (This file is gitignored so your key remains private.)

- **`requirements.txt`**: Python dependencies.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your username/Swarms-Emergence-Integration.git
cd Swarms-Emergence-Integration
```

### 2. Create a Python Virtual Environment (Optional)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

*(On Windows PowerShell: `.\.venv\Scripts\activate`.)*

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- [Swarms](https://github.com/kyegomez/swarms)
- [Swarms Models](https://pypi.org/project/swarm-models/)
- [Swarms Memory](https://pypi.org/project/swarms-memory/)
- [Requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### 4. Add Your `.env` File

Create a file named `.env` in the same directory:

```
EMERGENCE_API_KEY="<your-emergence-key>"
```

This environment variable is used by the EmergenceAgent to make API calls to the web orchestrator.

*(The `.env` file is listed in `.gitignore` to prevent committing secrets.)*

### 5. Run the Script

```bash
python main.py
```

When prompted, enter a **web automation prompt**—for instance:
```
Please go to CNN.com and find the latest AI investment news.
```

- The Swarms agent processes your request
- It uses the Emergence web orchestrator to perform web automation
- The script prints the final answer to your console

### 6. Verify or Debug

- If you see `No Emergence API Key configured...`, check your `.env` file
- If you see "Error creating Emergence workflow," verify your:
  - Internet connection
  - Emergence AI subscription status
  - API key validity

---

## File-by-File Summary

- **`EmergenceAgent.py`**  
  Defines the integration between Swarms and Emergence AI. Shows how to:
  1. Load environment variables with `python-dotenv`
  2. Create and poll Emergence web workflows
  3. Wrap Emergence functionality in a Swarms agent

- **`main.py`**  
  Entry point that demonstrates how to:
  1. Initialize the Swarm client
  2. Create an EmergenceAgent instance
  3. Process user input and handle responses

- **`swarm/__init__.py`**  
  Local module containing core classes:
  - `Agent`: Base class for creating agents
  - `Swarm`: Main orchestrator class
  - `Result`: Data structure for agent responses

- **`.env`**  
  Contains your `EMERGENCE_API_KEY`. Not committed to source control.

- **`requirements.txt`**  
  Lists all Python dependencies needed for the project.

- **`README.md`**  
  (This document!) Explains how to set up and run the integration.

--- 
