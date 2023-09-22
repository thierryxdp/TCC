def repetidos(list_num):
    """
    	retorna o número de vezes que um elemento é igual ao seu antecessor em dada lista
    	list -> int
    """
    qnt_repet=0
    i=1
    while i<len(list_num):
        if list_num[i]==list_num[i-1]:
            qnt_repet+=1
        i+=1
    return qnt_repet