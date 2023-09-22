def repetidos(lista):
    '''Escreva uma lista de numeros entre []. Caso algum desses 
    numeros for igual ao seu antecessor, a funcao conta o numero
    de vezes que isso ocorre.
    list -> int'''
    i=1
    contador=0
    while i<len(lista):
        if lista[i-1]==lista[i]:
            contador=contador+1
        i=i+1
    return contador