def repetidos(lista):
    contador = 0
    teste = 0
   	lista = ()
    while contador<len(lista):
        if lista[contador]==lista[contador-1]:
            teste = teste+1
        contador = contador +1
    return teste