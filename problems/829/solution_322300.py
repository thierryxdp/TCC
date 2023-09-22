def soma_h(n):
    """calcula e retorna o valor H com n termos dado,
    onde n deve ser inteiro
    int-> float"""
    control=list(range(1,n+1))
    for val in control:
        list.remove(control,val)
        list.append(control,1/val)
    return round(sum(control),2)