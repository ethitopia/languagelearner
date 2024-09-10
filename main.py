from learning.dialogue_manager import DialogueManager #class to be defined 
import json 


def load_scenarios(): 
    """
    Loads language scenarios from scenarios.json 
    """
    with open('scenarios.json', 'r') as file: 
        return json.load(file)
   
   
def select_scenario(scenarios): 
    """
    Selects a scenario from scenario options within scenarios.json
    
    Args: 
        scenarios (): represents option loaded from scenarios.json
    
    Returns: 
        scenario of user's choice  
    """
    print('Select a scenario:')
    for idx, scenario in enumerate(scenarios, 1): 
        print(f"{idx}. {scenario['scenario_name']}")
    choice = int(input("Enter your choice: ")) - 1
    return scenarios[choice]
   

def main(): 
    """
    main function, initializes program 
    """
    scenarios = load_scenarios() 
    selected_scenario = select_scenario(scenarios)
    dialogue_manager = DialogueManager(selected_scenario) # class to be defined 
    
    print("Starting scenario:", selected_scenario['scenario_name'])
    dialogue_manager.run_dialogue() 
    
    while True: 
        action = input("Type 'restart' to play again or pick another scenario /n Type 'exit' to quit: ")
        if action == 'restart': 
            scenarios = load_scenarios() 
            selected_scenario = select_scenario(scenarios)
            dialogue_manager = DialogueManager(selected_scenario) # class to be defined 
            
            print("Starting scenario:", selected_scenario['scenario_name'])
            dialogue_manager.run_dialogue() 
        elif action == 'exit': 
            break 
            

if __name__() == "__main__": 
   main() 
   
