def repetidos(lista=[]):
    '''Esta função através de uma lista de números, retorna as
    vezes que um elemento da lista é igual ao elemento anterior.
    assinatura list -> int'''
    valor = 0
    for i in range(len(lista)):
        if i > 0 and lista[i]==lista[i-1]:
            valor+=1
    return valor