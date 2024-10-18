def test_password(correct_password: str) -> bool:
    password = input("Introduce la contraseña: ")
    if correct_password == password:
        return True
    else:
        return False

def main():
    correct_password = "pasword123"
    
    if test_password == True:
        print("Contrasñea correcta")
    else:
        print("Contraseña incorrecta")
        


if __name__ == "__main__":
    main()
