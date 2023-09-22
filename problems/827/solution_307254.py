def qtd_divisores(numero):
    """retorna quantos divisores o numero informado tem.
    int->int"""
    qtd=0
    for elemento in range(1, numero+1):
        if numero%elemento==0:
            qtd= qtd+ 1
        else:
            qtd