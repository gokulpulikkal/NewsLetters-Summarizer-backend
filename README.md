# NewsLetters-Summarizer-backend

This project is a Flask-based API that processes news data and uploads it to Firebase Firestore.

## Project Structure

## Setup

1. **Clone the repository:**

    ```sh
    git clone git@github.com:gokulpulikkal/NewsLetters-Summarizer-backend.git
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venvForFlask
    source venvForFlask/bin/activate  # On Windows use `venvForFlask\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Add Firebase credentials:**

    Place your Firebase credentials file (`firebaseAuth.json`) in the root directory of the project.

## Running the Application

1. **Start the Flask application:**

    ```sh
    python api/index.py
    ```

2. **Access the application:**

    Open your browser and navigate to `http://127.0.0.1:5000/`.

## API Endpoints

### `POST /processText`

Processes the provided news data and uploads it to Firebase Firestore.

**Request Body:**
"""
{
    "news": [
        {
            "heading": "string",
            "detailed_news": "string",
            "time_to_read": "integer",
            "link": "string",
            "category": "string"
        }
    ]
}
"""
