def repetidos(lista):
    """Funcao que recebe como entrada uma lista de numeros e retorna o numero
    	de vezes sque um elemento da lista e igual ao elemento anterior"""
    indice=1
    contador=0
    flagSequencia=False
    while indice<len(lista):
        if lista[indice]==lista[indice-1]:
            flagSequencia=True
        else:
            flagSequencia=False
        if flagSequencia:
            contador+=1
        indice+=1
    return contador