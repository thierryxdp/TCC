def colchao(medidas,H,L):
    '''Funcao que, dada uma lista (medidas) com as dimensoes de um colchao, dispostas de forma crescente, a altura H e largura L de uma porta, retorna True se o colchao puder passar pela porta e False se não puder; list (int, int, int), int, int -> bool'''
    [a,b,c]=medidas
    if (c<H and a<L) or (b<L and c<H) or (b<L and a<H) or (b<H and a<L) or (a<H and c<L) or (b<H and c<L):
        return True
    else: 
        return False