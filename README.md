# Send Bulk Email and fetch data from CSV.
Send bulk email and fetch contents from CSV.

I made this project to help security team in my workplace to send credentials to all employees of the company (~700) personally with attachment of how to sign up.

# Instructions
1. Setup sender's email ID (if not done already).
2. Setup App Password: Don't use your email login credentials for the program since it won't work. Go to account settings > Security > 2-Step Authentication > App Password. Generate and app password and save it somewhere since you can't fetch the same afterwards.
3. Edit the email content to your liking. Save the file.
4. Generate .EXE file using Pyinstaller library. Command for the same is mentioned in further description.
5. Run the program.
6. The program will ask for path of CSV file to fetch data from and path of Email Attachment. Make sure to not put the path in quotes ("") or ('').
7. The CSV file should contain 'Name', 'Username', 'Password', 'Email Address'. But you can change that from line 43 in runme.py.
8. Next, paste the sender's email address and app password.
9. Confirm the activity and hit enter.
10. The process will begin and emails sent will be displayed with name and their respective email address in realtime.
11. There will be a CSV file generated automatically if the program is unable to send data to that particular email, then their entire row with all the data will be stored in another CSV called "failed.csv". This can be used to send details manually or to rerun the program for the faileds users avoiding duplicacy.
12. A log file 'log.txt' will be generated in case anything goes wrong, the exception handler will catch the error and store in the log file to refer later.

# Create Virtual Environment of Python
1. Install Python from microsoft store (For ex. Python 3.9)
2. This should be your python directory, copy it:
   C:\Users\Sushil\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0
3. On start menu, search "Environment Variables"
4. Go to System Variables>Path>Edit>New
5. Now paste the path in the field.
6. Click OK.
7. Open CMD in the desired directory you want to create your virtual environment
8. Type in the commands:
   python -m venv venv
9. And then:
   venv\Scripts\activate
10. You're now in your virtual environment. Now, install the python libraries mentioned in the description.
    Eg:
    pip install pyinstaller

# Generate .EXE
1. Save the .py file after making desirable changes(don't forget to add '/n' in the content if required to jump to next line.).
2. Create a virtual environment and install 'Pyinstaller' python library in it.
3. Open cmd and activate your virtual environment where you installed Pyinstaller.
4. Put the following command in CMD:
```
Pyinstaller --console --onefile runme.py
```
This will create a single .EXE file for your program and will store in a 'dist' folder present in the same directory as your virtual environment.

# Libraries used
pyinstaller <br>
yagmail <br>
csv <br>
os <br>

# Note
The contents of the email are dummy data for security reasons. Change the content to your liking and continue.

# Author
Sushil Waghmare <br>
Email: sushilwaghmare2048@gmail.com
