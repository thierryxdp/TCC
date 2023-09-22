def colchao(medidas,H,L):
    '''A funcao calcula se o colchao comprado passa pela
    porta. Digite as medidas do colchao dentro de [], da menor
    para a maior. Apos isso, digite a Altura e Largura da porta,
    respectivamente.
    #parametros | in: list (lista com as medidas do colchao, da
    menor para maior), float, float (medidas da porta) ->
    out: bool (True caso o colchao passe, False caso NAO passe.'''
    if (medidas[0]<=H or medidas[0]<=L) and (medidas[1]<=H or medidas[1]<=L):
        return True
    else:
        return False