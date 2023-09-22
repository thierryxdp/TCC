def maiores(numeros,n):
    """retorna uma nova lista com todos os numeros maiores que n presentes na lista passada;
    list,int -> list"""
    
    list.append(numeros,n)
    list.sort(numeros)
    i=list.index(numeros,n)
    return numeros[i+1:]