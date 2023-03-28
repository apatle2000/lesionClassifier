This is for running the lesion Classifer project.

The project has 2 main parts and is recomended to be run on a virtual enviornment.

a. backend:
    Its a Django frame work based on Python for easer implimetation of the Neural network models implimentations.
b. frontend:
    Its a React framework made by facebook( get used to errors and non-linear code) 


Steps to start up the entire project:

    1. Start the virtual enviornment (venv)
        windows : activate venv
        mac : source venv/bin/activate
    
        Note: to deactivate virtual enviornment : deactivate venv 
    

    2. Starting the backend server (Django server)
        a. Navigate to path: source_path/backend/lesionclassifier
        b. To run server on localhost port 8000 use command : python manage.py runserver 8000
    

    3. Starting the frontend server (React server): 
        a. Navigate to path: source_path/frontend/lesion
        b. To run server on localhost use comand : npm start or yarn start 
