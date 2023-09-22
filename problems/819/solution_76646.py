def filtraMultiplos(*listan):
    """Retorna uma outra lista contendo todos os elementos da lista
    original que forem divisiveis por n, dados: uma lista de numeros e
    um numero(n)."""
    
    valores_lista=listan[0]
    inteiro=listan[1]
    divisiveis=[]
    contador=0
    while contador<len(valores_lista):
        if valores_lista[contador]%inteiro==0:
            divisiveis.append(valores_lista[contador])
        contador+=1
    return divisiveis