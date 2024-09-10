import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_language_prompt(language, scenario):
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


if __name__ == "__main__":
    language = "Italian"
    scenario = "ordering food at a restaurant"
    result = generate_language_prompt(language, scenario)
    print(f"Generated Dialogue: \n{result['dialogue']}")
