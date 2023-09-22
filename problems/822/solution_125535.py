def repetidos(lis):
    """Função que recebe como entrada uma lista de números e retorna o número de vezes que o elemento da lista é igual ao elemento anterior"""
    """list-->int"""
    x=1
    z=0
    while x<len(lis):
        if lis[x]==lis[x-1]:
            z+=1
        x+=1
    return z