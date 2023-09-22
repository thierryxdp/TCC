def faltante(lista):
    'função que encontra um numero(int) faltando em uma lista de numeros que não repetem'
    contador=1
    lista_num=0
    list.sort(lista)
    while contador == lista[lista_num]:
        contador+=1
        lista_num+=1
    return contador