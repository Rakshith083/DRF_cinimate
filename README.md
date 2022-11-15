# DRF_cinimate
A Movie review rest-Api project developed using django rest framework.  

Project Setup
1. Install postgresql and pg admin on your machine, configure the username and password.
2. Replace username and password in .env file
3. Open the project folder in VS code and run the below commands

    #Install the required packages
    > pip install -r requirements.txt
    
    #Create database migrations
    > python manage.py makemigrations
    
    #Create tables in Database
    > python manage.py migrate
    
    #Run the server
    > python manage.py runserver
