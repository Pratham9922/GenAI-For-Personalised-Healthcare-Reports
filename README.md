Create a virtual environment in the project directory
`python -m venv env`

activate the virtual environment 
` env\Scripts\activate`

Install dependencies:

`pip install -r requirements.txt`

Then run the following for frontend app:

`cd front-end`
`streamlit run app.py`

On a new terminal window, run the following for backend:
`cd back-end`
`uvicorn main:app --reload`

