def repetidos(lista):
    
#Funcao que, dado uma lista de numeros, retorna o numero de vezes que um elemento da lista e igual ao elemento anterior.
    

    contador = 0
    acumuladora = 0
    

    while contador < len(lista)-1:
        if lista[contador+1] == lista[contador]:
            acumuladora += 1
        contador += 1

    return acumuladora