Calculation API
This is a simple Django REST Framework application for performing basic calculations. The API allows you to add two numbers and retrieve a list of all calculations performed. Additionally, there is an endpoint to generate and process calculation data from a JSON file.

Installation
Clone the repository:

bash
Copy code
git clone <repository-url>
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Apply the migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
API Endpoints
1. Add Numbers
URL: /add_numbers/

Method: POST

Request Body:

json
Copy code
{
    "operand1": 1,
    "operand2": 10
}
Response:

json
Copy code
{
    "id": 1,
    "operand1": 1,
    "operand2": 10,
    "sum": 11,
    "multiplication": 10,
    "division": 0.1,
    "timestamp": "2024-01-22T12:00:00Z"
}
2. Get All Data
URL: /get_all_data/

Method: GET

Response:

json
Copy code
[
    {
        "id": 1,
        "operand1": 1,
        "operand2": 10,
        "sum": 11,
        "multiplication": 10,
        "division": 0.1,
        "timestamp": "2024-01-22T12:00:00Z"
    },
    ...
]
3. Calculation JSON View
URL: /calculation_json/
Methods: GET, POST
GET
Response:

json
Copy code
{
    "message": "JSON file created",
    "file_path": "/path/to/calculation_data.json"
}
POST
Request Body:

json
Copy code
{
    "file_path": "/path/to/calculation_data.json"
}
Response:

json
Copy code
{
    "message": "File path processed successfully",
    "results": [
        {
            "operand1": 1,
            "operand2": 10,
            "sum": 11,
            "multiplication": 10,
            "division": 0.1
        },
        ...
    ]
}
Notes
Ensure that the Django development server is running before making API requests.
The Calculation model stores the details of each calculation, including operands, sum, multiplication, division, and timestamp.
The CalculationJsonView allows you to generate a JSON file with sample data and process it to perform calculations.
Feel free to explore and use these API endpoints for your calculation needs!






