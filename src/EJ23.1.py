def test_age(age: int):
    
            if age < 0:
                raise ValueError("La edad no puede ser negativa!")
            if age == 0:
                raise ValueError("La edad no puede ser cero!")
            if age > 125:
                raise ValueError("La edad no puede ser mayor a 125!")
            
def ask_age() -> int :
    age = None
    while age == None:
        try:
            age = int(input("Introduzca su edad: "))
            test_age(age)
        except ValueError as e:
            if age is None:
                print(f"***ERROR** El numero introducido no es valido!. Intentelo de nuevo!!!")
            else:
                print(f"***ERROR*** {e}. Intentalo de nuevo!!!")
            age = None
    return age

def show_age(age: int):
    for i in range (1, age + 1):
        print (i)

def main():
    age = ask_age()
    if age != None:
        show_age(age)
                
if __name__ == "__main__":
    main()