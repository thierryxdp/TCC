def repetidos(num):
    i=0
    qtd=0
    while i < len(num):
        if (num[i]==num[i+1]):
            qtd=qtd+1
        i=i+1
    return qtd