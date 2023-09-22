def repetidos(lista):
    '''A função recebe uma lista de números e retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior.
    Parâmetro de entrada: list
    Valor de retorno: int'''
    i=0
    iguais=0
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            iguais=iguais+1
        i=i+1
    return iguais