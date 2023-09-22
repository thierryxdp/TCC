def colcaoporta(lista, Hporta,Lporta):
    dim1,dim2,dim3=lista
    if dim1*dim2<Hporta*Lporta:
        return True
    elif dim2*dim3<Hporta*Lporta:
        return True
    elif dim1*dim3<Hporta*Lporta:
        return True
    else:
        return False