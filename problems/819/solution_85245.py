def filtraMultiplos(l,n):
    """recebe como entrada uma lsita de numeros e um numero, e retorna outra
    lista contendo todos os elementos da lista original que forem divisiveis por n"""
    
    m=0
    h=[]
    while m<len(l):
        if l[m]%n==0:
            h+=l[m]
        m+=1