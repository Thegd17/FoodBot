🍛 Saffron Delight (FoodBot)

An AI-Powered Food Ordering System built with FastAPI, Dialogflow, and Supabase.

📜 Project Overview

Saffron Delight is a full-stack food ordering application that combines a modern, responsive frontend with an intelligent chatbot backend. Users can browse a royal Indian menu, chat with an AI assistant to place orders naturally, and track their order status in real-time.

🌟 Live Demo

🚀 View Live Project on Vercel

✨ Key Features

🗣️ NLP Chatbot: Powered by Google Dialogflow, capable of handling complex orders (e.g., "1 Pav Bhaji and 2 Mango Lassi").

🛒 Order Management: Supports adding items, removing items, and completing orders with total price calculation.

📦 Order Tracking: Users can track order status using their Order ID.

🗄️ Database Persistence: All orders and tracking statuses are stored in Supabase (PostgreSQL).

🎨 Modern Indian UI: A responsive website featuring a "Royal Maroon & Saffron" theme with smooth AOS animations.

⚡ Fast Backend: Built with FastAPI for high-performance asynchronous request handling.

📂 Directory Structure

SaffronDelight/
│
├── main.py                  # 🚀 Entry point (FastAPI App & Webhook)
├── db_helper.py             # 🗄️ Database connection & logic
├── generic_helper.py        # 🛠️ Utility functions (Session extraction)
├── index.html               # 🌐 Main Frontend Interface
├── requirements.txt         # 📦 Python Dependencies
├── vercel.json              # ☁️ Vercel Deployment Config
├── .env                     # 🔒 Environment Variables (Not committed)
│
└── static/                  # 🎨 Frontend Assets
    ├── style.css            # CSS Styling
    ├── script.js            # Frontend Logic
    └── images/              # Menu Images (Optimized JPG/WebP)


🛠️ Tech Stack

Frontend: HTML5, CSS3 (Flexbox/Grid), JavaScript (ES6), Dialogflow Messenger.

Backend: Python 3, FastAPI, Uvicorn.

Database: Supabase (PostgreSQL).

AI Engine: Google Dialogflow ES.

Deployment: Vercel.

🚀 Local Setup & Installation

Follow these steps to run the project locally on your machine.

1. Clone the Repository

git clone [https://github.com/your-username/saffron-delight.git](https://github.com/your-username/saffron-delight.git)
cd saffron-delight


2. Install Dependencies

Make sure you have Python installed.

pip install -r requirements.txt


3. Environment Configuration

Create a .env file in the root directory and add your Supabase credentials:

SUPABASE_URL=[https://your-project-id.supabase.co](https://your-project-id.supabase.co)
SUPABASE_KEY=your-anon-public-key


4. Database Setup (Supabase)

Run the following SQL in your Supabase SQL Editor to create the necessary tables and functions:

-- 1. Create Tables
CREATE TABLE orders (
    order_id INT,
    item_id INT,
    quantity INT,
    total_price DECIMAL(10,2),
    PRIMARY KEY (order_id, item_id)
);

CREATE TABLE order_tracking (
    order_id INT PRIMARY KEY,
    status TEXT
);

CREATE TABLE food_items (
    item_id SERIAL PRIMARY KEY,
    name TEXT,
    price DECIMAL(10,2)
);

-- 2. Create Helper Function
CREATE OR REPLACE FUNCTION insert_order_item(
    p_food_item TEXT,
    p_quantity INT,
    p_order_id INT
)
RETURNS VOID AS $$
DECLARE
    v_item_id INT;
    v_price DECIMAL(10,2);
BEGIN
    SELECT item_id, price INTO v_item_id, v_price
    FROM food_items
    WHERE LOWER(name) = LOWER(p_food_item);

    IF v_item_id IS NOT NULL THEN
        INSERT INTO orders (order_id, item_id, quantity, total_price)
        VALUES (p_order_id, v_item_id, p_quantity, p_quantity * v_price);
    ELSE
        RAISE EXCEPTION 'Item % not found', p_food_item;
    END IF;
END;
$$ LANGUAGE plpgsql;


5. Run the Server

Start the FastAPI server:

uvicorn main:app --reload


Backend: Running at http://127.0.0.1:8000

Frontend: Visit http://127.0.0.1:8000 in your browser.

6. Connect Dialogflow

Use ngrok to expose your local server: ngrok http 8000

Go to Dialogflow Console > Fulfillment.

Enable Webhook and paste the ngrok URL (e.g., https://xxxx.ngrok.io/).

📸 Screenshots

Home Page

Royal Menu

Chatbot Interface

(Add screenshot here)

(Add screenshot here)

(Add screenshot here)

🔮 Future Improvements

[ ] Add Payment Gateway integration (Stripe/Razorpay).

[ ] User Authentication (Login/Signup).

[ ] Admin Dashboard to manage orders.

[ ] Multi-language support in Chatbot.

👨‍💻 Author

Gaurav Dhangar

AIML & Data Science
