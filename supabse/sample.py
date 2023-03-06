
import os
from supabase import create_client, Client

url: str = os.environ.get("https://zlqdcexdkusavjhmtabt.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpscWRjZXhka3VzYXZqaG10YWJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzgwOTM5ODEsImV4cCI6MTk5MzY2OTk4MX0.jyHhp_vguBWxn4BLl5YbgVKvBWsWi2nUoiz8xVFxXYs")
supabase: Client = create_client(url, key)

response = supabase.table('games').select("*").execute()

