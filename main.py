import data.connection as connection
import data.models     as models
import state
import getpass

def main():
    connection.global_init()
    try:
        while True:
            show_menu()
    except KeyboardInterrupt:
        return

def show_menu():
    print(40*'*')
    if state.logged_in:
        print('Menu : ')
        print('[1] Show list')
        print('[2] Add list')
        print('[3] Logout')
        print('[0] Exit')
        menu = input('Select menu : ')
        if menu in ['0', 'exit', 'exit()']:
            print('Bye...')
            raise KeyboardInterrupt
        elif menu == '1':
            show_list()
        elif menu == '2':
            add_list()
        elif menu == '3':
            logout()
        else:
            print(40*'*')
            print('Unknown Command')
    else:
        print('Menu :')
        print('[1] Login')
        print('[2] Register')
        print('[0] Exit')
        menu = input('Select menu : ')
        if menu in ['0', 'exit', 'exit()']:
            print('Bye...')
            raise KeyboardInterrupt
        elif menu == '1':
            login()
        elif menu == '2':
            register()
        else:
            print(40*'*')
            print('Unknown Command')

def register():
    print(40*'*')
    print('Register')
    username = input('Username : ')
    password = getpass.getpass('Password : ')

    if models.find_user(username) or username == '':
        print(40*'*')
        print('Username not available')
        return

    models.create_user(username, password)
    print(40*'*')
    print('Successfully Registered')
    return

def login():
    print(40*'*')
    print('Login')
    username = input('Username : ')
    password = getpass.getpass('Password : ')

    user = models.find_user(username)
    if not user or user.password != password:
        print(40*'*')
        print('Auth failed')
        return
    
    state.logged_in = user
    print(40*'*')
    print('Login successfully')

def logout():
    state.logged_in = None
    print(40*'*')
    print('Logout successfully')
    return

def show_list():
    print(40*'*')
    print('Not Implemented')
    return

def add_list():
    print(40*'*')
    print('Not Implemented')
    return

# -----------------------------------------------

if __name__ == '__main__':
    main()
