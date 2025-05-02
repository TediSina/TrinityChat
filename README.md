# TrinityChat

Hybrid AI-Human Chat for Customer Support using Django. (TODO)

## Description

Hybrid AI-Human Chat for Customer Support using Django... (TODO)

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

4. **Install Tailwind CSS Dependencies**

    ```bash
    python manage.py tailwind install
    ```

5. **Run Migrations**

    ```bash
    python manage.py migrate
    ```

6. **Start the Tailwind Development Server**

    Open a terminal and run:

    ```bash
    python manage.py tailwind start
    ```

7. **Start the Django Development Server**

    In another terminal, run:

    ```bash
    python manage.py runserver
    ```

8. **Access the Website**

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
