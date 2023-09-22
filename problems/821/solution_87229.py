def fatorial(n):
    """Recebe um número e retorna o fatorial desse mesmo número
    parâmetro de entrada:int
    parâmetro de saída:int"""
    número=int(input("Fatorial de: ") )
    resultado=1
    count=1
    while count <= numero:
        resultado=resultado*count
        count=count+1
    return resultado