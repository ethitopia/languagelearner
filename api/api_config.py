import openai
import os


class gptCient: 
    
    def __init__(self, api_key): 
        """
        Initialize the GPT client with the provided API key.
        
        Parameters:
            api_key (str): Your OpenAI API key for making requests.
        """
        self.api_key = api_key
        openai.api_key = self.api_key
        

    def generate_language_prompt(self, language, scenario):
        """
        Generates a learning dialogue or scenario in the specified language using OpenAI API.
        
        Parameters:
            language (str): The target language for the learner (e.g., 'Italian', 'Japanese').
            scenario (str): The specific real-world scenario (e.g., 'ordering food at a restaurant').

        Returns:
            dict: A structured response with dialogue or language learning prompts.
        """
        try:
            prompt = f"Teach me how to handle the following scenario in {language}: {scenario}. Provide a dialogue with explanations of cultural context and key phrases."
            
            response = openai.Completion.create(
                model="gpt-4",
                prompt=prompt,
                max_tokens=500,
                temperature=0.7,
                n=1
            )
            
            dialogue = response.choices[0].text.strip()
            return {
                "language": language,
                "scenario": scenario,
                "dialogue": dialogue
            }

        except Exception as e:
            print(f"Error generating prompt: {e}")
            return {
                "language": language,
                "scenario": scenario,
                "dialogue": "Error occurred during prompt generation."
            }

