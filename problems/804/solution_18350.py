def filtra_pares(x1,x2,x3,x4):
    '''Esta função recebe uma tupla e retorna uma nova tupla com somente os números pares da tupla original.
    tuple,tuple-->tuple'''
    tupla_nova=tuple()
    
    if x1%2==0 and x2%2==0 and x3%2==0 and x4%2==0:
        return tupla_nova+(x1,x2,x3,x4)
    elif x1%2==0 and x2%2==0 and x3%2==0:
        return tupla_nova+(x1,x2,x3)
    elif x1%2==0 and x2%2==0 and x4%2==0:
        return tupla_nova+(x1,x2,x4)
    elif x2%2==0 and x3%2==0 and x4%2==0:
        return tupla_nova+(x2,x3,x4)
    elif x1%2==0 and x3%2==0 and x4%2==0:
        return tupla_nova+(x1,x3,x4)
    elif x1%2==0 and x2%2==0:
        return tupla_nova+(x1,x2)
    elif x1%2==0 and x3%2==0:
        return tupla_nova+(x1,x3)
    elif x1%2==0 and x4%2==0:
        return tupla_nova+(x1,x4)
    elif x2%2==0 and x3%2==0:
        return tupla_nova+(x2,x3)
    elif x2%2==0 and x4%2==0:
        return tupla_nova+(x2,x4)
    elif x3%2==0 and x4%2==0:
        return tupla_nova+(x3,x4)
    elif x1%2==0:
        tupla_nova1=tupla_nova+(x1,)
        return tupla_nova1
    elif x2%2==0:
        tupla_nova2=tupla_nova+(x2,)
        return tupla_nova2
    elif x3%2==0:
        tupla_nova3=tupla_nova+(x3,)
        return tupla_nova3
    elif x4%2==0:
        tupla_nova4=tupla_nova+(x4,)
        return tupla_nova4
    else:
        return tupla_nova