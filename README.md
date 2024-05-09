community_website_backend/
│
├── controller.py # Main Python backend application file
├── templates/ # Directory containing HTML templates
│ ├── submitform.html # Homepage
│ ├── about.html # About page
│ ├── library.html # Library page
│ ├── post_form.html # Form for user share post submissions
│ └── contact.html # Contact page
└── README.md # Project README file

## Running the Application
1. Make sure you have Python installed on your system.
2. Install Flask using `pip install Flask`.
3. Navigate to the `community_website_backend/` directory.
4. Run the Flask application using the command `python app.py`.
5. Access the website by navigating to `http://127.0.0.1:5000` in your web browser.

## Routes
- `/`: Homepage
- `/about.html`: About page
- `/library.html`: Library page
- `/post_form.html`: Form for user submissions
- `/contact.html`: Contact page

## Form Submission
- The `/submitform` route handles form submissions from the `post_form.html` page.
- Upon form submission, the backend receives the form data and can process it as needed.

## Dependencies
- Flask: A lightweight web framework for Python.

## Contributors

- [Web Designer]
Simranjeet Kaur
