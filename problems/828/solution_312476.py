def primo(n):
    '''função que dado um numero inteiro positivo, retorna um valor booleano que indica que esse numero é primo ou nao
    entrada:int
    saida: bool'''
    if n%2 == 0:
        return False
    else:
        i = 3
        while(i < n):
            if n%i == 0:
                return False
            i = i+1
        return True