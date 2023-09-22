def repetidos(n:list)->int:
    '''Função que recebe uma lista e retorna  quantas vezes ele se repete com o anterior na lista'''
    i=0
    while i< len(n):
        if n[i]==n[i-1]:
        total = total+[1]
        i=i+1
    return len(total)