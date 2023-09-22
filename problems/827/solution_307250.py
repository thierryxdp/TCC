def qtd_divisores(numero):
    """retorna quantos divisores o numero informado tem.
    int->int"""
    indice=0
    for elemento in range(1, numero+1):
        if numero%elemento==0:
            indice = indice+ 1
        else:
            return indice