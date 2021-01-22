# Filed-Python-flask-API

## Project Description
process client payment with validating info provided .

## Getting Started

### Installing Dependencies

#### Python 3.8

Install the latest version of python for your platform.

#### Virtual Environment

working within a virtual environment keeps dependencies for the project separate and organized.

#### PIP Dependencies

Once we have your virtual environment setup and running, install dependencies by running:
```bash
pip install -r requirements.txt
```

This will install all of the required packages
##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [Flask-SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 
- [Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/) is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)  is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. 

## Database Setup
With Postgres running, restore a database using the filed.psql file provided. From the backend folder in terminal run:
```bash
psql filed < filed.psql
```
Or create your own database and change the database_name in src\models\models.py 

## Data Migration & Running the server

From within the `\src` directory first ensure you are working using your created virtual environment.
First import our app to flask, execute:
```bash
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=true
```
Then make data migration:
```bash
flask db init
flask db migrate
flask db upgrade
```
To run the server, execute:

```bash
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app` directs flask to use the `app.py`.

## Assumptions:
- since we have three different payment gateways which are external services api so I assumed that it could be simulated as sending the data to database.
- 3 tables are created in our database to simulate the three payment gateways.
- the payment follow the business rules provided
## How The API Works?
- a request of payment is received from the client side.
- all provided data is validated.
- a control function receive the data and send it to the correct gateway according to the payment amount.
- data stored in database as a simulation for payment accepted.
## Tests:
### Postman
- Go to url `https://web.postman.co/`
- login and open workspace
- upload filed-python-flask collection from `/filed-python-flask.postman_collection.json`
- test each scenario.
### unit test:
- included database name 'filed_test' upon use restore db from filed_test.psql
- run `src\unit_test\unit_test.py`
## API References

### Getting Started

##### Base URL: 
Currently hosted locally at http://127.0.0.1:5000/.

##### Authentication: 
Currently no Auth needed.

### Error Handling:

Errors are returned as JSON objects in the following format:
```bash
{
    "success": False,
    "error": 400,
    "message": "Bad Request!!!! Please make sure the data you entered is correct"
}
```
The API will return error types when requests fail, example:
```bash
400: Bad Request
500: Internal Server Error
```
### Endpoints
##### POST '/payment'

- Function: process and validate user payments with the external services
- Requested Arguments: CreditCardNumber(string), CardHolder(string), ExpirationDate(datetime), SecurityCode(string:optional)& Amount(float)

- Returns an object with success and custom message as follows:
```
{
    "message": "Payment is processed",
    "success": true
}
```


