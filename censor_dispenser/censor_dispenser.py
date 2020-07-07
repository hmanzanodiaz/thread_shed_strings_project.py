# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_one(string):
    email_one.strip("learning algorithms")
    print(email_one)

censor_one("learning algorithms")

cp -R /Users/env70284/code_academy/projects/"email_two.txt" /Users/env70284/code_academy/projects/censor_dispenser

