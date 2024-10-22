def  pedir_edad():
    age = int(input("Introduce tu edad: "))
    return age

def comprobar_edad(age: int) -> bool:
    age = age
    if age >= 18:
        return True

def main():
    age = pedir_edad()
    if comprobar_edad(age):
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    

if __name__ ==  "__main__":
    main()