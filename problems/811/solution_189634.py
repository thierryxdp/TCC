def colchao(colchao,h,l):
    """Função que compara o colchão com a porta"""
    if colchao[1] <= h:
        return True
    elif colchao[2]<=l:
        return True        
    else:
        return False