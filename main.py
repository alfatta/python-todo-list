def main():
    try:
        while True:
            show_menu()
    except KeyboardInterrupt:
        return

def show_menu():
    print(20*'*')
    print('Menu :')
    print('[1] Login')
    print('[2] Register')
    print('[0] Exit')
    menu = input('Pilih menu : ')
    print()
    if menu in ['0', 'exit', 'exit()']:
        print('Bye...')
        raise KeyboardInterrupt
    elif menu == '1':
        login()
    elif menu == '2':
        register()
    else:
        print(20*'*')
        print('Perintah tidak dikenali')

def register():
    print(20*'*')
    print('--- Not Implemented ---')
    input('Press any key to continue...')
    print()

def login():
    print(20*'*')
    print('--- Not Implemented ---')
    input('Press any key to continue...')
    print()

# -----------------------------------------------

if __name__ == '__main__':
    main()
