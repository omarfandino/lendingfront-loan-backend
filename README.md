# Welcome to Loan Backend

Welcome to our online loan application portal! We're here to help you secure the funding your business needs to thrive. Please fill out the form with the required details, and we'll promptly evaluate your application.

If you prefer to interact with our endpoints directly, you can do so using [Postman](https://www.postman.com/).

## Request Details

| Method | URL                                                     | Body (Example)                                                                                       | Description           |
| ------ | ------------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------- |
| GET    | https://lendingfront-loan-backend.onrender.com/api      |                                                                                            | Returns a simple greeting |
| POST   | https://lendingfront-loan-backend.onrender.com/api/loan | `{ "tax_id": "12345678-9", "business_name": "LendingFront", "request_amount": "4000000" }` | Reviews if we can provide a loan for the requested amount |

## If you are a developer

1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/omarfandino/lendingfront-loan-backend
   ```
2. Navigate into the cloned repository folder:
   ```sh
   cd lendingfront-loan-backend
   ```
3. Rename the `.env.example` file to `.env`

4. Ensure you have [Python](https://www.python.org/) installed on your machine.

5. **(Optional)** We recommend installing virtual environments to execute the project, but if you prefer not to, you can skip this step.
   - Open a terminal and run the following commands:
		|macOS/Linux|Windows|
		|-|-|
		|`python3 -m venv .venv`|`py -3 -m venv .venv`|
		|`. .venv/bin/activate`|`.venv\Scripts\activate`|
	>For more information, visit the following link: [Virtual Environments](https://flask.palletsprojects.com/en/3.0.x/installation/#virtual-environments)

6. Open a terminal and run the following commands:
	```sh
	pip install -r requirements.txt
	python run.py
	```

7. The project should now be accessible at `http://localhost:5000/api`
