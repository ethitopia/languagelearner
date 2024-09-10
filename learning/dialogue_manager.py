
class DialogueManager: 
    """
    Manages dialogue with GPT prompts and modeling 

    Args: 
        scenario (string): string indicating scenario selected 
    """
    def __init__(self, openai_client, user_language):
        self.openai_client = openai_client
        self.user_language = user_language
    
    
    def start_conversation(self, user_input): 
        system_prompt = f"You are teaching {self.user_language} to a learner. "
        return self.openai_client.chat(system_prompt, user_input)
    
    
        
         
    