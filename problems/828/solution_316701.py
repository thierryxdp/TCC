def qtd_divisores(numero):
    '''funçao que dado um numero inteiro retorna seus divisores.
int -> lista'''
    quant=[]
    lixeira=[]
    for c in range(numero+1):
        if c==0:
            lixeira.append(c)
        elif numero%c==0 :
            quant.append(c)
    return len(quant)

def primo(numero):
    quant=qtd_divisores(numero)
    if quant==2:
        return True
    else:
        return False