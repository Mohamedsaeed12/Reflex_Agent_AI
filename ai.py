#Mohamed Saeed   
# 1/03/2025
# purpose = Simple Reflex Agent for cleaning blocks 

def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"  # clean the current spot
    elif location == "A":
        return "Right"  # move to B
    else:
        return "Left"  # move to A

def run_simulation():  # number of steps needed and all the possible option
    allOption = [ #all possible options
        ("A", "Clean", "Clean"),
        ("A", "Dirty", "Clean"),
        ("A", "Clean", "Dirty"),
        ("A", "Dirty", "Dirty"),
        ("B", "Clean", "Clean"),
        ("B", "Dirty", "Clean"),
        ("B", "Clean", "Dirty"),
        ("B", "Dirty", "Dirty"),
    ]
    steps = 2 #steps
    for check in allOption:  #runs through each example 
        agent_Location, status_a, status_b = check
        print(f"Initial configuration: Agent at {agent_Location}, A: {status_a}, B: {status_b}")
        
        environment = {"A": status_a, "B": status_b}#statics if block is clean or dirty
        total_score = 0

        for a in range(steps):
            # give points for clean squares at the start of each step
            total_score += sum(1 for state in environment.values() if state == "Clean")

            # agent check and acts on the infomation given
            status_check = environment[agent_Location]
            action = simple_reflex_agent(agent_Location, status_check)
            print(f"Agent at {agent_Location}, perceives {status_check}. Action: {action}")

            # update the environment
            if action == "Suck":
                environment[agent_Location] = "Clean"
            elif action == "Right":
                agent_Location = "B"
            elif action == "Left":
                agent_Location = "A"

        # clean test check for last step
        total_score += sum(1 for state in environment.values() if state == "Clean")

        print(f"Final environment: {environment}, Total Score: {total_score}\n")

# Run the simulation
run_simulation()
