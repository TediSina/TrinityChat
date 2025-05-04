# 🧠 TrinityChat – Hybrid AI-Human Customer Support for Baboon

**Junction X Tirana 2025 — Challenge: Hybrid AI-Human Chat (by Baboon)**  
**Team: Code Trinity**  
**Members:** Tedi Sina (Backend), Klerti Malaj (Frontend), Sara Kaçi (Marketing)

TrinityChat is an intelligent customer support platform designed to streamline and elevate the way Baboon engages with its users. Built during Junction X Tirana 2025 by the three-member team Code Trinity, this system blends AI automation with real-time human intervention—ensuring both speed and empathy in customer support.

Using a smart session tracking system, TrinityChat allows Baboon’s support operators to monitor and take over conversations previously handled by an AI chatbot. Admins can seamlessly switch sessions to “human mode” when needed, view chat history in real-time, and access order history to assist users more effectively. All of this is managed through a clean and intuitive admin dashboard.

## 🚀 Technologies Used

- **Django** (backend framework)  
- **Tailwind CSS & daisyUI** (frontend styling)  
- **PostgreSQL** (relational database)  
- **Vercel** (deployment platform)  

## 🔑 Key Features

- 💬 **Live chat system** powered by hybrid AI-human interaction  
- 🧑‍💻 **Operator dashboard** with session selector, chat history, and reply interface  
- 📜 **Order history display** for informed customer support  
- 🔄 **Real-time updates** for messages and session statuses  

TrinityChat embodies the future of customer service for platforms like Baboon—intelligent, responsive, and human-centered.

## How to Run the Development Server

To set up and run the development server, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/TediSina/TrinityChat.git
    cd ammaf
    ```

2. **(Optional) Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set the environment variables**

    Create a `.env` file in the root directory of the project then set the variables down below (set the default values for SQLite3):

    ```env
    SECRET_KEY = 'YOUR_SECRET_KEY_HERE'
    GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY_HERE'
    DB_ENGINE = 'YOUR_DATABASE_ENGINE_HERE' # Default: 'django.db.backends.sqlite3'
    DB_NAME = 'YOUR_DATABASE_NAME_HERE' # Default: ''
    DB_USER = 'YOUR_DATABASE_USER_HERE' # Default: ''
    DB_PASSWORD = 'YOUR_DATABASE_PASSWORD_HERE' # Default: ''
    DB_HOST = 'YOUR_DATABASE_HOST_HERE' # Default: ''
    DB_PORT = 'YOUR_DATABASE_PORT_HERE' # Default: ''
    ```

5. **Install Tailwind CSS Dependencies**

    ```bash
    python manage.py tailwind install
    ```

6. **Run Migrations**

    ```bash
    python manage.py migrate
    ```

7. **Start the Tailwind Development Server**

    Open a terminal and run:

    ```bash
    python manage.py tailwind start
    ```

8. **Start the Django Development Server**

    In another terminal, run:

    ```bash
    python manage.py runserver
    ```

9. **Access the Website**

    Open your web browser and navigate to `http://127.0.0.1:8000` to view the website.

## Notes

- Ensure you have Python and Django installed on your system.
- Tailwind CSS and daisyUI are pre-configured with Django-Tailwind.
- Any additional configurations or environment variables required for development should be specified in the `.env` file (e.g. `SECRET_KEY` & `GEMINI_API_KEY`).
- The Tailwind and Django development servers need to be run side by side (at the same time).

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome and appreciated!

## License

MIT License

Copyright (c) 2025 Tedi Sina, Klerti Malaj & Sara Kaçi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
