def repetidos(lista):
    "recebe uma lista de numeros e retorna quantas vezes um numero foi sucedido por ele mesmo"
    x=1
    n=0
    while x<len(lista):
        if lista[x]==lista[x-1]:
            n=n+1
        x=x+1
    return n