def primo(numero):
    """dado um número inteiro e positivo, a função retorna True se ele for
    primo e False caso contrário.
    int-->bool
    
    Parâmetros
    numero: número inteiro e positivo, que será julgado como primo ou não."""
    contador=0
    for elemento in range(1,numero+1):
        if numero%elemento==0:
            contador=contador+1
    if contador<=2:
        return True
    else:
        return False