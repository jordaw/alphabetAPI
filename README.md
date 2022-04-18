<h1 align="center">AlphabetAPI</h1>

<p align="center">A simple <a href="https://www.django-rest-framework.org/"> Django REST</a> API that receives an input string, and determines if the string contains at least one of each letter of the alphabet.</p>

## Pertitnent Files
- Alphabet logic, GET/POST logic - **alphabet/api/views.py**
- Test files for expected true/false inputs - **alphabet/api/tests**
- Serializer to convert request data to JSON - **alphabet/api/serializers.py**
- URL dispatcher, registers API application routes - **alphabet/api/urls.py**
- Database object - **alphabet/api/models.py**

## Running Locally

1. Clone repository
1. Create a virtual environment in base directory and activate

   ~~~~
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ~~~~

1. Install Django, Django REST framework, and other necessary dependencies into the virtual environment

   ~~~~
   pip install -r requirements.txt
   ~~~~

1. Run DB migrations
   
   ~~~~
   cd alphabet/
   python manage.py migrate
   ~~~~

1. (Optional) Create a superuser to access admin page (localhost:8000/admin/)

   ~~~~
   python manage.py createsuperuser
   ~~~~
   
1. (Optional) Run tests

   ~~~~
   python manage.py test -v 2
   ~~~~

1. Run server (localhost:8000/api/alphabet/check)
   
   ~~~~
   python manage.py runserver
   ~~~~
