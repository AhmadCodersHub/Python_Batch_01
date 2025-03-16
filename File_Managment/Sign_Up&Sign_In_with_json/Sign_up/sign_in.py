import json

def read_data():
    with open('data.json','r') as f:
        json_resp = json.load(f)
        all_data = json_resp.get('all_data',[])
        return all_data
    
def save_data(previous_data):
    with open('data.json','w') as f:
        json.dump(fp=f,obj={'all_data':previous_data},indent=4)

def sign_up(user_name,email,password):
    all_data = read_data()
    all_emails = [data.get('email') for data in all_data]

    if email in all_emails:
        print('Email already exists!')
    else:
        previous_data = all_data
        data = {
            'name':user_name,
            'email':email,
            'password':password
        }
        previous_data.append(data)
        save_data(previous_data)
        print('Sign Up Successfully! Welcome',user_name)

def sign_in(email,password):
    all_data = read_data()
    for data in all_data:
        name = data.get('name')
        if data.get('email') == email and data.get('password') == password:
            print('Login Successfully! Welcome',name)
            break
            
    else:
        new_user = input('Do you want to sign up? (yes/no): ')
        if new_user.lower().strip() == 'yes':
            user_name = input('Enter your name:- ')
            sign_up(user_name,email,password)
        else:
            print('Login Failed. Please try again!')
    



email = input('Enter your email: ')
password = input('Enter your password: ')
sign_in(email,password)