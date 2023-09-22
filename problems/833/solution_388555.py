def conta_numero(n,matriz):
    """Função que dada uma matrz de inteiros, conta e retrorne quantas vezes aquele
    n° aparece na matriz; int,int=>int"""
    	x = 0
        for linha in matriz:
            x = x + list.count(linha,n)
            return x