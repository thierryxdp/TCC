def primo(n):
    '''Função que verifica se um número é primo ou não;
    int -> bool'''
    div=[]
    for i in range(1,n+1):
        if n%i == 0:
            list.append(div, i)
            if len(div) > 2:
                return False
    if len(div) == 2:
        return True