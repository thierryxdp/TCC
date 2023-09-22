def repetidos(num):
    i=1
    qtd=0
    while i < len(num):
        if (num[i-1]==num[i]):
            qtd=qtd+1
        i=i+1
    return qtd