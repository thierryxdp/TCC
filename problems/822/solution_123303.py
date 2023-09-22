def repetidos(lista):
    contador = 0
    tamanhoLista= len(lista)
    for numero in lista:
        if numero == lista[1]:
            contador +=1
        return contador