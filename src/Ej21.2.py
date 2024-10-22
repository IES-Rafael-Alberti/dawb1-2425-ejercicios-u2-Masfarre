def test_password(password: str) -> bool:
    if password == "password":
        return True
    else:
        return False
def ask_pasword() -> str:
    password = input("Introduce tu contraseña: ")
    return password

def main():
    password = ask_pasword().lower().strip()
    if test_password(password) == True:
        print("Contrasñea correcta")
    else:
        print("Contraseña incorrecta")
        


if __name__ == "__main__":
    main()
