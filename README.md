# Database-Lab_-Joy-Student
Joy Student is a student information management system, which allows information registration, 
forum chatting and adding friends, etc. 



# Lopullinen palautus/ Final submission: 

The Joy Student system facilitate users below operations: 


to create user account (username and password), 


to login and logout the system, 


to maintain the user account (update username and passwords), 


to delete registered info, 


to register personal information,


to update and display the registered personal information,


to write messages to the chat forum for text communication,


to like the messages posted in the forum by clicking like button, or cancel the like by another clicking.


to view how many likes received for each message. 


to add another student as friend based on known User ID, being aware who is in the system.



It contains 5 database tables.  Currently the program’s frame and main operations can work well. The user interface and appearance of the application are finished. The application works well in testing. If the user provides incorrect information, a clear notification will appear.

The application can only be tested locally as follows: 


1). Clone the repository to local device. 


2). Create an .env file there.


3). Specify its contents:


DATABASE_URL='database-local-url'
SECRET_KEY='secret-key'


4). Activate the virtual environment and install the dependencies:


python3 -m venv venv
source venv/bin/activate (“venv” visible in front of the command line)
pip install -r ./requirements.txt


5). Define the database schema: psql < schema.sql


6). Startup with the command: flask run


Below are intermediate submissions 




# Välipalautus 3/ Submission 3

Add a new feature that users can send messages, which is similar as a chat application. requirements.txt and schema.sql files pushed to Github.

Currently the program’s frame and main operations can work well, still need to improve the functionability. The user interface and appearance of the application are finished. The major part of application works when the user tests it. It is clear to the user what the functions of the application do. If the user provides incorrect information, a clear notification will appear.

The application can only be tested locally as follows: 
1). Clone the repository to local device. 
2). Create an .env file there.
3). Specify its contents:
DATABASE_URL='database-local-url'
SECRET_KEY='secret-key'
4). Activate the virtual environment and install the dependencies:
python3 -m venv venv
source venv/bin/activate (“venv” visible in front of the command line)
pip install -r ./requirements.txt
5). Define the database schema: psql < schema.sql
6). Startup with the command: flask run




# Välipalautus 2/ Submission 2

Programming work started after the 1st submission. Target is to program the application that it has a functional foundation. Few problems have been fixed by practice. For example, PostgreSQL database was not able to find the server after installation, configuring the database connections was hard in the beginning as the local servers can not display html pages. 

Features of the application refined after the 1st submission: 
1.  the user can log in and log out, and create a new user account. 
2.  The user can use form to submit info, and form elements are mainly text fields and checkboxes.
3.  Each user is a basic user who can login to resubmit or modify the data. 
4.  Total 5 webpages will be visible for the user: homepage(index.html) offering two options (create account or login), login page for users who have already account credentials, register page for those who needs to create account, result page for users to view registered info, error page to display the failed operations.
5.  The web application should be able to display the registered student's name, gender, faculty, student number, and address. Those are the information the user can view and modify after submitting information in the form. 

Structure and completed files till now: 
1.  app.py is the main module of the application, which launches the application. 
2.  The module db.py takes care of things related to the database. In this application, this module determines the address of the database and creates a db object through which the database can be accessed.
3.  The task of module routes.py is to process page requests. 
4.  Users.py module is used to handle users data management.
5.  Error, index, login, register total 4 html pages created in templates folder. Result page after registration still to be done.
6.  The connection between pages still to be done so that page is able to jump to next page. 

How to startup the application: 
Navigate to the project file directory in local device, use command line enter flask run, the webpage content will be visible by visiting the local host address: http://127.0.0.1:5000/



# Välipalautus 1/ Submission 1  
The topic is to create a light student information management system, named Joy Student. 

The system can be used by a school or university to manage student's data. Features of the application include:
1.  the user can log in and out, and create a new user account. 
2.  The user can use form to submit info, and form elements are mainly text fields and checkboxes.
3.  Each user is a basic user who can login to resubmit or modify the data. 
4.  total 3 webpages will be visible for the user: Homepage, register page(that is the page1.html for filling personal info), result page (this is the result.html for showing the filled personal info). 
5.  The web application should be able to display the registered student's name, gender, faculty, student number, and address. 
    Those are the information the user can view after submitting information in the form. 

This web application can be enhanced by adding further features or functions, like provide a field for submitting student's email address, 
The language used in programming will be English. In order to ensure the language consistency, all documents in this course will also be in English.














