def primo(numero):
    '''funcao que verifica se numero e primo.'''
    '''int+>int'''
    dvezes=0
    for n in range(2,numero):
        if numero% n ==0:
            dvezes+=1
    if dvezes == 0:
        return(True)
    else:
        return (False)