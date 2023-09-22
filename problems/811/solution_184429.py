def colchao(medidas,H,L):
    """Função que dados as medidas das dimensões A,B,C de um colchão em 
       centímetros e ordenadas da menor para a maior e a 
       altura H e a largura L da porta que passará o colchão, retorna true 
       se o colchão consegue passar pela porta e false se não consegue.
       list,int,int->bool.
       
       Parâmetros: 
       medidas: Uma lista com as dimensões do colchão da menor para a maior.
       H: A altura da porta.
       L: A largura da porta.
       
       returns: True se o colchão consegue passar pela porta e false se não
                consegue.
    """
    [A,B,C] = medidas
    if C>max(H,L) and B>min(H,L):
        return true
    else:
        return false