def colchao(lista, Hporta,Lporta):
    """Essa função retorna se uma porta de dimensões Lporta e Hporta é grande o suficiente
    para passar um colchão de dimensões dim1,dim2 e dim3. 
    
    list, int,int -> Bool
    
    exemplos:
    colchao([20,20,20],20,20)==True"""
    dim1,dim2,dim3=lista
    if dim1<=Hporta and dim2<=Lporta:
        return True
    if dim1<=Hporta and dim3<=Lporta:
        return True
    if dim2<=Hporta and dim3<=Lporta:
        return True
    if dim1<=Lporta and dim2<=Hporta:
        return True
    if dim1<=Lporta and dim3<=Hporta:
        return True
    if dim2<=Lporta and dim3<=Hporta:
        return True
    else:
        return False