def colchao(medidas,H,L):
    """retorna se é possivel que um colchão passe pela porta, dadas as medidas
       do colchão, da menor para a maior, e a altura e largura da porta"""
    if (((medidas[0]))<=H and ((medidas[1]))<=L) or (((medidas[0]))<=L and ((medidas[1]))<=H)>:
        return "True"
    else :
        return "False"