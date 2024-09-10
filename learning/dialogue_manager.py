import json 

class DialogueManager: 
    """
    Manages dialogue with GPT prompts and modeling 

    Args: 
        scenario (string): string indicating scenario selected 
    """
    def __init__(self, openai_client, user_language):
        self.openai_client = openai_client
        self.user_language = user_language
        
    
    def load_scenario(self, difficulty, scenario): 
        """
        Loads openai client prompt with user language, difficulty, and scenario
        
        Args: 
            difficulty (string): difficulty of chosen prompt
            scenario (string): scenario of chosen prompt 
            
        Returns: 
            language prompt 
        """
        language = self.user_language
        scenario = json.load(f'/scenarios/{difficulty}/{scenario}')
        return self.openai_client.generate_language_prompt(language, scenario)
        
    
    def start_conversation(self, user_input): 
        system_prompt = f"You are teaching {self.user_language} to a learner. "
        return self.openai_client.chat(system_prompt, user_input)
    
    
        
         
    