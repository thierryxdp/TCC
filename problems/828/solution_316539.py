def primo(num):
    """dado um número, a função retorna True se esse número for primo ou Falso
    se não for;
    int->int"""
    qtde_divisores=0

    for numero in range(1,num+1):
        if num%(numero+1)==0:
            qtde_divisores=qtde_divisores+1
    if qtde_divisores==2:
        return True
    else:
        return False