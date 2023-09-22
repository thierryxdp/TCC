def colchao(medidas,H,L):
    """retorna true se o colchao passa pela porta e false caso nao 
    passe, dado as medidas do colchao, altura e largura da porta.
    list,int,int --> bool"""
    
    lado1,lado2,lado3=medidas[0],medidas[1],medidas[2]
    if ((lado1<=L and lado2<=H) or (lado1<=H and lado2<=L)) or ((lado1<=L and lado3<=H) or 
    (lado3<=L and lado1<=H)) or ((lado3<=L and lado2<=H) or (lado2<=L and lado3<=H)):
        return true
    else:
        return false