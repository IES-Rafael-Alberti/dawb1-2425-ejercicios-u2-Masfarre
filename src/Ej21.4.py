def ask_num() -> int:
    num =  None

    while num is None:
        try:
            num = int(input("Introduce un numero: "))
        except ValueError:
            print("**ERROR** Numero invalido. Intentalo de nuevo")
    return num

def main():
    num = ask_num()
   
    if num % 2 == 0:
        print(f"El numero {num}, es par")
    else:
        print(f"El numero {num}, es impar")

if __name__ == "__main__":
    main()

