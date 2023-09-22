def maiores(n,m):
    """ Função que exclui os números, inteiros a partir de um
    número que pertence a mesma lista
    list-> list"""
    
    n.append(m)
    n1 = sorted(n)
    n2 = n1.index(m)
     
    del(n1[0:n2+1])
    return n1