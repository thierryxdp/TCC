def colchao (medidas,h,l):
    """Calcula e retorna a possibilidade ou não do colchao entrar na casa do Joao, dado a altura(h) e largura da porta(l) mais as dimensoes do colchão (a,b,c); float --> str"""
    medidas==[a,b,c]
    if c<=h and a<=l:
        return 'True'
    elif c>h and b<=l:
        return 'True'
    elif b<=h:
        return 'True'