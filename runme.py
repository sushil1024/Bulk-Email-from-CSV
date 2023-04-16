import csv
import yagmail
import os

def sendmail(emailid, name, username, password, senderemail, senderpass, attachment):

    with open("logs.txt", 'a+') as output_file:
        try:
            # credentials of sender
            yag = yagmail.SMTP(senderemail, senderpass)

            # details of the email
            yag.send(
                to=emailid,
                subject="Web Authentication: Essential Security Measure for Office Internet Access",
                contents=f"Dear {name}, \n\n Please use the following credentials to sign in: \n\n Username: {username} \n Password: {password} \n\n ",
                attachments=attachment,
            )

            print(f"Credentials sent successfully to {name} on email: {emailid}")
            output_file.write(f"Credentials sent successfully to {name} on email: {emailid}\n")

            return True

        except Exception as e:
            print(f"Failed to send email: {e}")
            output_file.write(f"Failed to send email: {e}\n")
            output_file.write(f"Name: {name} email: {emailid}\n")
            return False


def readfile(csvfile, attachment):

    with open('failed.csv', 'a+', newline='') as file:
        writer = csv.writer(file)

    # CSV file import
    with open(csvfile, 'r') as file:
        reader = csv.DictReader(file)
        
        # Column names to match your CSV file
        for row in reader:
            name = row['Name']
            username = row['Username']
            password = row['Password']
            email = row['Email Address']

            emailsent = sendmail(email, name, username, password, senderemail, senderpass, attachment)

            if not emailsent:
                temp = []
                for value in row.values():
                    temp.append(value)

                with open('failed.csv', 'a+', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(temp)


if __name__ == "__main__":

    file_path = input("Paste path of CSV file: ")

    attachment = input("Paste path of email attachment: ")

    header = ['Name', 'Username', 'Password', 'Email Address']
    with open('failed.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

    with open("logs.txt", 'a+') as output_file:

        if os.path.isfile(file_path):
            try:
                print("File read successful!")
                output_file.write("File read successfully!\n")

                senderemail = input("\nEnter sender's email ID: ")
                senderpass = input("Enter sender's password: ")

                ch = input("Are you sure you want to send the emails?(y/n)")
                ch = ch.lower()
                if ch != 'y':
                    print("Exiting..!")
                    exit()

                readfile(file_path, attachment)
            except Exception as e:
                print(f"Error reading CSV file: {e}")
                output_file.write(f"Error reading CSV file: {e}\n")

        else:
            print("File does not exist or is not valid.")
            output_file.write("File does not exist or is not valid.\n")

    input("Press Enter to exit!")
