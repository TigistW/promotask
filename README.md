# Promo Code System

A Django-based promo code system that allows generating and applying promo codes with a 60% discount.

## Endpoints

### Generate Promo Code

- **URL**: `/promo/generate/`
- **Method**: `POST`
- **Response**:
  ```json
  {
    "code": "XXXXXXXX",
    "discount": 60.0,
    "usage_count":0
  }
### Generate Promo Code With Discount Amount

- **URL**: `/promo/generate/`
- **Method**: `POST`
- **Request**:
  ```json
  {
    "discount": 60.0,
  }

- **Response**:
  ```json
  {
    "code": "XXXXXXXX",
    "discount": 60.0,
    "usage_count":0
  }


### Apply Promo Code

- **URL**: `/promo/apply/<code>/`
- **Method**: `POST`
- **Response**:
  - **Success**:
    ```json
    {
      "message": "Promo code applied successfully!",
      "discount": 60.0,
      "usage_count": 3
    }
    ```
  - **Failure**:
    ```json
    {
      "message": "Invalid promo code."
    }
    ```

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```
   This command clones the repository to your local machine. Replace `<repository-url>` with the actual URL of the Git repository.

2. **Navigate to the project directory**:
   ```bash
   cd PromoCodeSystem
   ```
   This command changes the directory to the project folder, which should be the name of the repository or project.

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   This command installs the required Python packages listed in the `requirements.txt` file.

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```
   This command applies any database migrations necessary for the Django application to function properly.

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```
   This command starts the Django development server, allowing you to access the application locally.

## Notes

In this section:
- The setup steps are listed in an ordered list.
- Code blocks for commands like cloning the repository, navigating to the directory, installing dependencies, applying migrations, and running the server are properly formatted using triple backticks (`` ``` ``) and specifying the language (e.g., `bash`) for syntax highlighting.

This is correctly formatted in Markdown and should display as expected in any Markdown viewer.
```