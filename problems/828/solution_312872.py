def primo(num):
    """Função que dado um número inteiro positivo, verifica se o número é p
       primo ou não. Retorna valor booleano.
       int -> bool
       
       Parâmetros:
       num: número inteiro positivo que será verificado se é primo ou não.
       
       returns: True caso seja primo e False caso não seja
    """
    contador = 2
    lista = 0
    while contador < num and lista == 0:
        if num%contador == 0:
            lista += 1
        contador += 1
    if lista >= 1:
        return False
    else:
        return True