def ask_age() ->  int:
    age = None
    while age is None:
        try:
            age = int(input("Introduce tu edad: "))
        except ValueError:
            print("**ERROR** La edad introducida no es valida")
    return age

def ask_money() -> float:
    money = None
    while money is None:
        try:
            money = int(input("Introduce tus ingresos mensuales: "))
        except ValueError:
            print("**ERROR** El numero introducido no es valido")
    return money

def main():
    age = ask_age()
    money = ask_money()
    
    if age >= 16 and money >= 1000:
        print("Debes de tributar un determinado impuesto")
    else:
        print("No tienes que tributar")

if __name__ == "__main__":
    main()