import json
from src.slack import find_threads
from src.freshdesk import get_ticket_conversations
from src.claude import get_completion

ticket_id = 85551

threads = find_threads(ticket_id)
# print(threads)

conversations = get_ticket_conversations(ticket_id)
# print(conversations)

prompt = f"## Internal Slack discussion about ticket #{ticket_id}:\n\n{threads}"
prompt += f"\n===\n\n## Freshdesk conversation about ticket #{ticket_id}:\n\n{conversations}"
prompt += "\n===\n\nUsing the above context, and your own knowledge, please briefly summarize the root cause of the issue and the steps taken to resolve it. (100-200 words)"

# print(prompt)

response = get_completion(prompt)

print(response['completion'])