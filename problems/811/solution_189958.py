def colchao(medidas,H,L):
    
    [A,B,C]=medidas
    
    """
    Nomeia-se as medidas como pedido no enunciado e após isso deve-se 
    comparar as medidas A,B e C com o H e o L, onde caso 2 das medidas sejam
    uma menor que H e outra menor que L, o retorno seja True e o colchão
    passa pelas portas
    """
    
    if ((medidas[0]<=H) and (medidas[1]<=L)) or ((medidas[1]<=H) and (medidas[2]<=L)) or ((medidas[2]<=H) and (medidas[0]<=L)) or ((medidas[0]<=L) and (medidas[1]<=H)) or ((medidas[1]<=L) and (medidas[2]<=H)) or ((medidas[2]<=L) and (medidas[0]<=H)):
        return True
    else:
        return False