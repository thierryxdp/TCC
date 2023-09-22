def maiores(L1,n):
    """Funcao que dada uma lista L1 de numeros inteiros e um
    numero inteiro n, retorna outra lista, contendo todos
    os numeros da lista original maiores que n;
    lista,int->lista"""
    
    list.append(L1,n)
    list.sort(L1)
    Valor1=list.index(L1,n)
    Valor2=list.count(L1,n)
    Valor3=(Valor1+Valor2-1)
    
    return L1[Valor3:]