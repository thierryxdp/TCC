def filtraMultiplos(lis,x):
    """Função que recebe como entrada uma lista e um número x, retornando outra lista contendo todos os elementos da lista original que forem divsíveis por x"""
    """list,int-->list"""
    cont=0
    m=[]
    while cont<len(lis):
        if lis[cont]%x==0:
            m=m+[lis[cont],]
            cont=cont+1
    return m