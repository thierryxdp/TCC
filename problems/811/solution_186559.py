def colchao(m,ph,pl):
    """obtemos os valores das medidas do colchao, sabemos que podemos 
    virar o paralelepido, logo so precisamos que ele passe. Apos isso
    temos duas opcoes para que ele passe, se a porta for 
    maior que as medidas restantes ele ira passar, caso o contrario nao
    list,int,int - > bool"""
    if (ph>=m[0] and pl>=m[1]) or (pl>=m[0] and ph>=m[1]):
        return True
    else:
        return False