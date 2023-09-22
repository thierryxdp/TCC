def repetidos(num):
    """ Função que recebe uma lista com números e retorna
    a quantidade de vezes que o sucessor é igual ao
    antecessor.
    Entrada: lista
    Saída: int"""
    indice  = 0
    numero = 0 
    while indice < len(num)-1:
        if num[indice] == num[indice+1]:
            numero = numero + 1       
        indice = indice +1
    return numero