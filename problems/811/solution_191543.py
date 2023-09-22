def colchao(medidas,H,L):
    """ função que diante das medidas dadas
    do colchão , e a altura e largura de uma
    porta , ela irá determinar se o colchão
    passará por essa porta.
    assinatura: list,int,int --> bool
    testes:
    colchao([25,120,220],200,100)== True
    colchao([25,205,220],200,100)== False
    colchao([25,200,220],200,100)== True
    """
    a= medidas[0]
    b= medidas[1]
    c= medidas[2]
    medidas= [a,b,c,]
    if (b <=H) and (a<=L):
        return "True"
    elif (b <=L) and (a<=H):
        return "True"
    else:
        return "False"