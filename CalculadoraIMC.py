while True:
    Peso = input("Ingresa tu peso en kilogramos: ")
    Altura = input("ingresa tu altura en metros: ")
    try:
        float(Altura)
        float(Peso)
        if float(Altura) > 2.50:
            print("La altura que ingresaste no es valida...Error 1")
        elif float(Peso) > 700:
            print("El peso que ingresaste no es valido...Error 1")
        else:
            Altura2 = float(Altura) * float(Altura)
            Resultado = float(Peso) / float(Altura2)
            print(Resultado)
            input("Presiona ENTER para cerrar")
            break
    except ValueError:
        print("Debes de ingresar solamente numeros...Error 0")

