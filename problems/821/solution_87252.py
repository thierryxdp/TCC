def fatorial(numero):
    numero = int(input("Fatorial de: ") )
    resultado=1
    count=1
    while count<=numero:
        resultado=resultado*count
        count=count+1
    return (resultado)