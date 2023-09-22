def primo(n):
    '''funcao que verifica se um numero e primo ou nao;
    Entrada: int+
    Saida: bool'''
    div=0
    for i in range(n):
        if n%(i+1) == 0:
            div+=1
    if div<3:
        return True
    elif div>2:
        return False