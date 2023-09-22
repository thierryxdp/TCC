def filtra_pares(tupla):
    """Retorna uma nova tupla contendo apenas elementos pares da tupla anterior. Entrada -> tuple; Saída -> tuple"""
    
    if tupla[0]%2==0:
        a=(tupla[0],)

    else:
        a=()
        
    if tupla[1]%2==0:
        b=(tupla[1],)

    else:
        b=()

    if tupla[2]%2==0:
        c=(tupla[2],)

    else:
        c=()

    if tupla[3]%2==0:
        d=(tupla[3],)

    else:
        d=()

    return (a+b+c+d)