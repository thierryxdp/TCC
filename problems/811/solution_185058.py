def piramide_num(n1,n2):
    '''Função que dados dois números (n1,n2) retorna uma
    pirâmide de números. ex: (2,4) -> [2,3,4,3,2]
    int,int->list'''
    
    if (n2>n1):
        n2=n2+1
        sequencia=list(range(n1,n2))
        sequencia1= sequencia[:]
        sequencia2= sequencia[-2::-1]
        
    else:
        n1=n1+1
        sequencia=list(range(n2,n1))
        sequencia1= sequencia[-1::-1]
        sequencia2= sequencia[1:]
        
    return sequencia1+sequencia2