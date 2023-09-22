def repetidos(lista):
    """Funcao que, dado uma lista de numeros, retorna o numero de vezes que um elemento da lista é igual ao anterior
    list-->int"""
   	i = 0
    numero = 0
    list.sort(lista)
    while i<len(lista)-1:
        if lista[i+1]==lista[i]:
            numero=numero+1
        i=i+1
    return numero