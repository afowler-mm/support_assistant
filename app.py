import json
from src.slack import find_threads
from src.freshdesk import get_ticket_conversations

ticket_id = 81661

threads = find_threads(ticket_id)
print(threads)

# conversations = get_ticket_conversations(ticket_id)
# print(conversations)