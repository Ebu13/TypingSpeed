You need to go to the address "http://127.0.0.1:8000/rows" for the API created for the data in the Rows table


# FastAPI Typing Game Backend

This project serves as the backend for the Typing Game application, providing access to 
game data through API endpoints. The backend is developed using FastAPI and SQLite.

## Project Setup

1. Install the required dependencies by running the following command:

   ```bash
   pip install fastapi uvicorn sqlite3

2. Make sure you have the database.sqlite3 file containing the required data.

3. Start the FastAPI server using the following command:


   ```bash
   uvicorn main:app --reload
   ```
   

1. The API should be accessible at http://localhost:8000

    API Endpoints
    Get Rows
    URL: /rows
    
    Method: GET
    
    Description: Retrieves a list of rows containing sentence data for the typing game.
    
    Response Example:
      {
        "rows": [
          {
            "id": 1,
            "row_data": "I enjoy taking long walks on the beach and watching the sunset."
          },
          {
            "id": 2,
            "row_data": "The mountains are a place where I can find peace and serenity."
          },
          ...
        ]
      }



## CORS Configuration
Cross-Origin Resource Sharing (CORS) is configured to allow access from all origins for simplicity. 
For a more secure setup, modify the CORS configuration in main.py to specify allowed origins

## Notes
This project assumes you have a SQLite database named database.sqlite3 with a table named rows containing columns 
id and row_data. Additional API endpoints and features can be added to enhance the backend functionality 
based on your requirements.