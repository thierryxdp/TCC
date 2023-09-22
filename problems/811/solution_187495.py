def colchao(medidas,H,L):
    """Funcao que dado as medidas do colchao e da porta, retorna true se o colchao conseguir passar na porta e false se nao. list,int,int=>bool"""
    if medidas[1]<max(H,L) or medidas[3]<max(H,L):
        return True
    else:
        return False