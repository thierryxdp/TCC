def filtraMultiplos(L1,n):
    """Funcao que filtra os multiplos de um inteiro n. A 
    funcao recebe como entrada uma lista de numeros L1 e um
    numero n e retorna outra lista contendo todos os 
    elementos da lista original que forem divisiveis por n;
    lista, int->lista"""
    
    i=0
    L2=[]
    
    while i<len(L1):
        if L1[i]%2==0:
            L2=L2+[L1[i]]
        i=i+1
    return L2