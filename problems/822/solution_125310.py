def repetidos(num):
    """
    Recebe uma lista de numeros e retorna o numero de vezes
    que um elemento da lista é igual ao elemento anterior;
    list -> list
    """
    i=0
    lista_num=[]
    
    while i < len(num):
        lista_num = num.count(num[i])
    i = i+1
    return lista_num