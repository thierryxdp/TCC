def filtraMultiploz(listan):
    valores_lista = listan[0]
    inteiro = listan[1]
    divisiveis = []
    contador = 0
    while contador < len(valores_lista):
        if valores_lista[contador] % inteiro == 0:
            divisiveis.append(valores_lista[contador])
        contador+=1
    return divisiveis

def filtraMultiplos(lista,n):
    indice=0
    multiplos=[]
    while indice<len(lista):
        if lista[indice]%n==0:
            list.append(multiplos,lista[indice])
            indice=indice+1
        else:
            indice=indice+1
    return multiplos