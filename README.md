# Database-Lab_-Joy-Student
Joy Student is a student information management system. 

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
Thank you!












