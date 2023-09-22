def repetidos(n:list)->list:
    '''Função que recebe uma lista e retorna  quantas vezes ele se repete com o anterior na lista''''
    i=0
    total=[]
    while i< len(n):
        if n[i]==n[i-1]:
            list.remove(n,n[i])
            i=i+1
            return len(total)