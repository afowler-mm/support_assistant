import json
from src.slack import find_threads
from src.freshdesk import get_ticket_conversations

# threads = find_threads("86169")
# print(json.dumps(threads, indent=2))

conversations = get_ticket_conversations(85312)
print(json.dumps(conversations, indent=2))