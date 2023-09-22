def resto_divisao(n):
    return 1%n
def qtd_divisores(n):
    lista=[]
    for i in range(0,n+1):
        if resto_divisao(n)==0:
        	lista.append(i)
            i=i+1
    return len(lista)