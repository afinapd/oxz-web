# DemoQA Web Automation Testing

This project contains automated test cases for the DemoQA website using Python with Selenium WebDriver and Behave BDD framework.

## Video Execution
Watch the test automation in action:
[Click here to watch on GDrive Link](https://drive.google.com/file/d/1y4hNGlgx1kMnabsyiNRTl-ZJRHuyHRjS/view?usp=sharing)

## Features Tested

1. **Authentication**
   - Login with valid credentials
   - Login with invalid credentials
   - Error message validation

2. **Bookstore**
   - View list of books (public access)
   - View list of books (after login)
   - Search for specific books
   - Book details verification

3. **Profile Management**
   - Access profile without login
   - Logout functionality
   - Delete books from profile

## Prerequisites

- Python 3.8 or higher
- Chrome browser
- Virtual environment (recommended)

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
oxz-web/
├── features/
│   ├── pages/              # Page Object Models
│   │   ├── bookstore_page.py
│   │   ├── login_page.py
│   │   └── profile_page.py
│   ├── steps/              # Step Definitions
│   │   ├── authentication_steps.py
│   │   ├── bookstore_steps.py
│   │   └── profile_steps.py
│   ├── authentication.feature
│   ├── bookstore.feature
│   └── profile.feature
├── requirements.txt
└── README.md
```

## Running Tests

Run all tests:
```bash
behave -f pretty features/
```

Run specific feature:
```bash
behave -f pretty features/profile.feature
```

Run tests with tags:
```bash
behave -f pretty --tags=@test features/
```

## Test Reports

Test results are displayed in the console with the following information:
- Number of features passed/failed
- Number of scenarios passed/failed
- Number of steps passed/failed/undefined
- Total execution time

## Page Objects

The project follows the Page Object Model pattern:

- **BookstorePage**: Handles book listing, search, and navigation
- **LoginPage**: Manages authentication operations
- **ProfilePage**: Handles profile-related actions and book management