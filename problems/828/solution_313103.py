def primo(n):
    """verifica se um número dado como entrada é primo;int->bool"""
    lista=list(range(1,n+1))
    resposta=[]
    i=0
    while(i<len(lista)):
        if (n%lista[i]==0):
            list.append(resposta,i)
        i+=1
    return len(resposta)==2