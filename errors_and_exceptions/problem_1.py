try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print('Type Error! Watch out!')

try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print('Zero Division Error!')
except Exception as e:
    print(f'Something other than zero division wrong: {e}')
finally:
    print("code can still run")


def ask():
    while True:
        try:
            user_response = int(input("Enter a number"))
            print(user_response ** 2)
            break
        except:
            print('not an int')
            continue
        finally:
            print('completed')


ask()
