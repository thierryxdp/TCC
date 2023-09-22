def primo(num):
    """dado um número, a função retorna True se esse número for primo ou Falso
    se não for;
    int->int"""
    qtde_divisores=0
    if num==2:
        return False
    else:
        for numero in range(1,num):
            if num%(numero+1)==0:
                qtde_divisores=qtde_divisores+1
        if qtde_divisores==1:
            return True
        else:
            return False