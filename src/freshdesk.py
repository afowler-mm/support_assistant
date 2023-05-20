import requests
from config import freshdesk_api_token, freshdesk_domain
from bs4 import BeautifulSoup
from dateutil.parser import parse

# The function to get all the conversations for a ticket
def get_ticket_conversations(ticket_id):
    # Initialize variables
    page = 1
    all_conversations = []
    formatted_conversations = []

    while True:
        # Format the URL
        url = f"https://{freshdesk_domain}.freshdesk.com/api/v2/tickets/{ticket_id}/conversations?page={page}"
        
        # Send the GET request
        response = requests.get(
            url,
            auth=(freshdesk_api_token, 'X'),
            headers={"Content-Type": "application/json"},
        )

        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f"Request failed with status {response.status_code}")

        # Parse the response JSON
        conversations = response.json()

        # If the response is empty, break the loop
        if not conversations:
            break

        # Append the conversations to the main list
        all_conversations.extend(conversations)

        # Go to the next page
        page += 1

    # Format the conversations
    for conv in all_conversations:
        # Extract the text from the HTML body
        soup = BeautifulSoup(conv['body'], 'html.parser')
        body_text = soup.get_text(separator=' ').strip()
        
        # Format the timestamp
        timestamp = parse(conv['created_at']).strftime('%Y-%m-%d %H:%M:%S')

        # Prepare the from string based on 'incoming' value and 'from_email'
        if conv['incoming']:
            from_string = "CUSTOMER"
        else:
            from_string = f"AGENT {conv['from_email']}" if conv['from_email'] else "AGENT"

        # Add the formatted conversation to the list
        formatted_conversations.append(f"{from_string} ({timestamp}): {body_text}")

    return formatted_conversations
