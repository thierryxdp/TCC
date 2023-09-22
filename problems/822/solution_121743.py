def repetidos(num):
    """Para que seja retornado a quantidade de repetições de um
    número indicado, digite;
    int->int"""
    i = 1
    listai = []
    while i<len(num):
        if num[i] == num[i]:
            num.append(listai,num[i])         
        i += 1
        return len(listai)