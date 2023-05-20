import slack_sdk
from config import slack_api_token
from datetime import datetime

client = slack_sdk.WebClient(token=slack_api_token)
support_channels = ["support-general", "support-on-call"]

# find threads containing mention of this ticket number
def find_threads(ticket):
    threads = client.search_messages(query=ticket, sort="timestamp", sort_dir="desc", count=10)["messages"]["matches"]
    # ignore threads not in the support_channels
    threads = [thread for thread in threads if thread["channel"]["name"] in support_channels]

    if len(threads) == 0:
        return "No threads found."

    thread_string = ""
    # make a readable version of all the messages in each thread
    for thread in threads:
        thread_messages = client.conversations_replies(channel=thread["channel"]["id"], ts=thread["ts"])["messages"]
        readable_messages = []
        for message in thread_messages:
            # get user info
            user_info = client.users_info(user=message["user"])
            user_name = user_info["user"]["real_name"]
            
            # convert timestamp to datetime
            timestamp = datetime.fromtimestamp(float(message["ts"])).strftime('%Y-%m-%d %H:%M:%S')
            
            # format message
            readable_message = f"{user_name} ({timestamp}): {message['text']}"
            readable_messages.append(readable_message)
        
        thread["messages"] = readable_messages

        thread_string += "\n".join(readable_messages)
        thread_string += "\n\n"  # Add a separator between threads

    return thread_string
