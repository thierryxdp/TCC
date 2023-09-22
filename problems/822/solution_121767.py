def repetidos(nume):
    """Para que seja retornado a quantidade de repetições de um
    número indicado, digite;
    int->int"""
    i = 1
    listai = []
    while i<len(nume):
        if num[i] == nume[i-1]:
            listai+=[listai,nume[i]]         
        i += 1
    return len(listai)/2