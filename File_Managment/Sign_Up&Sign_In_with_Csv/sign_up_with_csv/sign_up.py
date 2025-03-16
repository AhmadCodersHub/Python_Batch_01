import csv


def all_save_emails(file_name):
    with open(file=file_name,mode='r') as file:
        reader = csv.reader(file)
        all_save_data = [row[1].lower().strip() for row in reader]
        return all_save_data

def save_data(file_name,new_user_data):
    with open(file=file_name,mode='a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_user_data)

def sign_up(all_emails,name,email,password):
    if email.lower().strip() in all_emails:
        print(F'\n[Error] - Email({email}) Already Takken!\n')
        return None
    else:
        new_user_data = [name,email,password]
        print(f'\n[INFO] Congratulation ({name}) Sign Up Successfully!\n')
        return new_user_data

file_name = 'data.csv'
print(f'\n[INFO] Welcome to Join Us........\n')
name = input('enter your name:- ')
email = input('enter your email:- ')
password = input('enter your password:- ')
all_emails = all_save_emails(file_name)
user_data = sign_up(all_emails,name,email,password)
if user_data:
    save_data(file_name,user_data)
