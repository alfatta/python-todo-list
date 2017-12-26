import data.connection as connection
import data.models     as models
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
    print('Menu :')
    print('[1] Login')
    print('[2] Register')
    print('[0] Exit')
    menu = input('Pilih menu : ')
    if menu in ['0', 'exit', 'exit()']:
        print('Bye...')
        raise KeyboardInterrupt
    elif menu == '1':
        login()
    elif menu == '2':
        register()
    else:
        print(40*'*')
        print('Perintah tidak dikenali')

def register():
    print(40*'*')
    print('Register')
    username = input('Username : ')
    password = getpass.getpass('Password : ')

    if models.check_user(username) or username == '':
        print(40*'*')
        print('Username not available')
        return

    models.create_user(username, password)
    print('Successfully Registered')
    return

def login():
    print(40*'*')
    print('--- Not Implemented ---')

# -----------------------------------------------

if __name__ == '__main__':
    main()
