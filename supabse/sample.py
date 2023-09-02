
import os
from supabase import create_client, Client

url: str = os.environ.get("supabase_url")
key: str = os.environ.get("your_DB_key")
supabase: Client = create_client(url, key)

response = supabase.table('games').select("*").execute()

