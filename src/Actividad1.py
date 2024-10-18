def comprobar_numero(entrada: str):
    if entrada.startswith("-"):
        entrada = entrada [1:]
    return entrada.isdigit

def introducir_numero(msj: str) -> (bool, int):
    entrada = input(msj).strip().lower

    if comprobar_numero(entrada):
        return True, int(entrada)
    else: 
        if entrada == "fin":
            return True, None
        else: 
            return False, None

def main ():
    cont = 0
    suma = 0
    media = 0

    salir = False

    while not salir:
        entrada_correcta, numero = introducir_numero("Introduzca un número: ")
        if entrada_correcta and numero is not None:
            cont += 1
            suma += numero
        elif entrada_correcta and numero is None:
            encuentra_fin = True
        else:
            print ("Entrada inválida")
    
    if cont > 0: 
        media = suma/cont
    
    print("{} {} {}".format(cont,suma,media))

if __name__ == "__main__":
    main()