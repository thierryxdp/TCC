def substitui(s,x,i):
    """essa função recebe tês entradas, uma palavra, uma letra e uma posição, e retorna a mesma palavra, porém com a letra escolhida substituindo a que ja estava na posição escolhida;
    str,str,int--->str"""
    s = list(s)
    s[i] = x
    return ''.join(s)