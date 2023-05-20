from config import anthropic_api_token
import anthropic

client = anthropic.Client(anthropic_api_token)

def get_completion(prompt):
    response = client.completion(
        prompt=f"{anthropic.HUMAN_PROMPT} {prompt}{anthropic.AI_PROMPT}",
        stop_sequences = [anthropic.HUMAN_PROMPT],
        model="claude-v1-100k",
        max_tokens_to_sample=600,
    )
    return response