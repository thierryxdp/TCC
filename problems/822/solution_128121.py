def repetidos(listn):
    '''funcao que recebe uma lista de numeros e retorna
    o numero de vezes que um elemento da lista é igual ao
    elemento anterior
    Parametros:
    List
    Saida:Int'''
    h=0
    p=0
    while p<len(listn):
        if listn[p]==listn[p+1]:
            h= h+1
        p=p+1
    return h