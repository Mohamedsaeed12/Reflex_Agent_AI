# Reflex_Agent_AI
🧹 Simple Reflex Agent Simulation
Author: Mohamed Saeed
Date: January 3, 2025
🧠 Purpose
This Python program simulates a Simple Reflex Agent that cleans two locations (A and B). It demonstrates basic AI agent behavior in a deterministic, fully observable environment—specifically, the Vacuum World problem commonly taught in introductory AI courses.

📜 Description
The agent senses whether the current location is Dirty or Clean.

If it's Dirty, it performs the action "Suck" to clean it.

If it's Clean, it moves:

Right if it’s in location A

Left if it’s in location B

The environment includes 2 locations (A and B), and the simulation tests all 8 possible initial configurations of the environment, such as:

Agent starts at A or B

A and/or B is Dirty or Clean

For each configuration:

The simulation runs for 2 steps

The agent receives 1 point per clean square per step

A final score is calculated based on the cleanliness of the environment

🧾 Files
simple_reflex_agent.py: The main script containing the agent logic and simulation runner.

▶️ How to Run
Make sure you have Python 3 installed. Run the script using:

bash
Copy
Edit
python simple_reflex_agent.py
💡 Sample Output
text
Copy
Edit
Initial configuration: Agent at A, A: Dirty, B: Dirty
Agent at A, perceives Dirty. Action: Suck
Agent at A, perceives Clean. Action: Right
Final environment: {'A': Clean, 'B': Dirty}, Total Score: 4
📈 Scoring System
For every step (including the final state), the agent earns 1 point per clean location.

Maximum possible score per scenario = (steps + 1) × 2 = 6

🔍 Concepts Demonstrated
Simple Reflex Agents

Agent-Environment interaction

Basic AI decision-making

State-space simulation

Performance measurement via score

🧩 Extensions (Optional Ideas)
Add random dirt generation at each step

Implement a Model-Based agent that remembers past states

Add more locations (e.g., grid world)

Track cumulative performance across multiple runs
