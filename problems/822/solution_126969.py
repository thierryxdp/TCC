def repetidos(lista):
    '''função que ddada uma lista de numeros, retorna o numero
    de vezes que um elemento da lista é igual ao elemento
    anterior.  ent-> list  saida->  int'''
    
    indice = 1
    resposta = 0
    
    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
            resposta = resposta +1
        indice = indice + 1
    return resposta