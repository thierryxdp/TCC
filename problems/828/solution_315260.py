def primo(numero):
    '''dado um número inteiro positivo retorna True se 
    ele for primo e False se não for um número primo.'''
    qdt_div=0
    for n in range(1,numero+1):
        if numero%n==0:
            qdt_div=qdt_div+1
    if qdt_div==2:
        return True
    else:
        return False