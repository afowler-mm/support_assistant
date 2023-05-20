import json
from src.search_slack import find_threads

threads = find_threads("86169")
print(json.dumps(threads, indent=2))
