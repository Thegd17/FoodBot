import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Retrieve the keys
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase credentials not found. Please check your .env file.")

# Initialize Supabase Client
supabase: Client = create_client(url, key)

def insert_order_item(food_item, quantity, order_id):
    try:
        # We send the TEXT name (p_food_item)
        # The SQL function will look up the ID and Price automatically!
        response = supabase.rpc('insert_order_item', {
            'p_food_item': food_item, 
            'p_quantity': quantity, 
            'p_order_id': order_id
        }).execute()

        print(f"Order item '{food_item}' inserted successfully!")
        return 1

    except Exception as e:
        print(f"Error inserting order item: {e}")
        return -1

def insert_order_tracking(order_id, status):
    try:
        data = {"order_id": order_id, "status": status}
        supabase.table("order_tracking").insert(data).execute()
        print(f"Order tracking inserted for {order_id}")
    except Exception as e:
        print(f"Error inserting order tracking: {e}")

def get_total_order_price(order_id):
    try:
        response = supabase.rpc('get_total_order_price', {
            'p_order_id': order_id
        }).execute()
        return response.data
    except Exception as e:
        print(f"Error getting total price: {e}")
        return 0

def get_next_order_id():
    try:
        response = supabase.table("orders") \
            .select("order_id") \
            .order("order_id", desc=True) \
            .limit(1) \
            .execute()
        
        data = response.data
        
        if not data:
            return 1
        else:
            return data[0]['order_id'] + 1
    except Exception as e:
        print(f"Error getting next order id: {e}")
        return 1

def get_order_status(order_id):
    try:
        response = supabase.table("order_tracking") \
            .select("status") \
            .eq("order_id", order_id) \
            .execute()
        
        data = response.data
        
        if data:
            return data[0]['status']
        else:
            return None
    except Exception as e:
        print(f"Error getting order status: {e}")
        return None