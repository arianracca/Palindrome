def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    print(is_palindrome(nombre))

nombre = input(str("Ingrese para chequear si es un palíndromo \n"))

if __name__ == '__main__':
    run()