def ask_gender() -> bool:
    gender = input("Introduce M si eres hombre o F si eres mujer: ").lower()

    while gender != 'm' and gender != 'f':
        gender = input(f"El genero introducido no es valido. \nIntroduce M si eres hombre o F si eres mujer: ").lower()
  
    return gender

def ask_name() -> str:
    name = input("Introduce tu nombre: ").lower()
    if 'a' <= name[0] <= 'm':
        return True
    else:  
        return False


def main():
    gender = ask_gender()
    name = ask_name()
    if (gender == "f" and  name == True) or (gender == "m" and  name == False):
        print("Estas en el grupo A")
    else:
        print("Estas en el grupo B")

if __name__ == "__main__":
    main()