def repetidos(listn):
    '''funcao que recebe uma lista de numeros e retorna
    o numero de vezes que um elemento da lista é igual ao
    elemento anterior
    Parametros:
    List
    Saida:Int'''
    h=0
    p=0
    b= p-1
    while p<len(listn):
        if listn[0]==listn[1]:
            h= h+1            
        if listn[p]==listn[b]:
            h= h+1
        p=p+1
    return h