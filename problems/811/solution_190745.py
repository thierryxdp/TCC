def colchao(x,h,l):
    """Função que retorna se é possível passar o colchao pela porta dada as medidas do colchão e altura e largura da porta"""
    """Tupla-->bol"""
    a=x[0]
    b=x[1]
    c=x[2]
    
    return a<=h or a<=l or b=<h or b<=l or c<=h or c<=l