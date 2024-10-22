def ask_num() -> int:
    num = None
    while num is None:
        try:
            num = float(input("Introduce un numero: "))
            test_num(num)
        except ValueError:
            print("El valor introducido es invalido!!")
            num = None
        except ZeroDivisionError as e:
                print(f"**ERROR**{e}")
                num = None
    return num

def test_num(num: float):
    if num == 0:
        raise ZeroDivisionError ("El valor introducido no puede ser 0")
    
def main():
    num1 = ask_num()
    num2 = ask_num()
    resultado = num1 / num2
    print(f"El resultado de {num1} / {num2} es: {resultado}")

if __name__ == "__main__":
    main()