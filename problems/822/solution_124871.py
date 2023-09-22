def repetidos(num):
    """essa função recebe uma lista de números, podendo conter 
    repetiçoes e retorna quantas vezes dentro da lista um valor
    é igual ao elemento do qual ele está sucedendo;
    list->int"""
    i = 1
    listai = []
    while i<len(num):
        if num[i] == num[i-1]:
            listai+=[listai,num[i]]         
        i += 1
    return len(listai)/2