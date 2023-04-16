# Bulk-Email-from-CSV
Send bulk email and fetch contents from CSV.

I made this project to help security team in my workplace to send credentials to all employees of the company (~700) personally with attachment of how to sign up.

# Instructions
1. Setup sender's email ID (if not done already).
2. Setup App Password: Don't use your email login credentials for the program since it won't work. Go to account settings > Security > 2-Step Authentication > App Password. Generate and app password and save it somewhere since you can't fetch the same afterwards.
3. Run the program.
4. The program will ask for path of CSV file to fetch data from and path of Email Attachment. Make sure to not put the path in quotes ("") or ('').
5. Next, paste the sender's email address and app password.
6. Confirm the activity and hit enter.
7. The process will begin and emails sent will be displayed with name and their respective email address in realtime.
8. There will be a CSV file generated automatically if the program is unable to send data to that particular email, then their entire row with all the data will be stored in another CSV called "failed.csv". This can be used to send details manually or to rerun the program for the faileds users avoiding duplicacy.
9. A log file will be generated in case anything goes wrong, the exception handler will catch the error and store in the log file to refer later.

# Author
Sushil Waghmare
sushilwaghmare2048@gmail.com
