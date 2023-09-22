def substitui(s,x,i):
    """Uma funcao que recebe uma str e um caractere x e um numero inteiro 1 entre 0 e o comprimento da str
    parametro: entradastr, int
    retorna: saida -> str"""
    
    if i<0 or i>1 len(s):
        return 'Insira um numero valido'
    else:
        return s[0:i]+x+s[i+1]