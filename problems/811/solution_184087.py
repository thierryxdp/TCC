def colchao(medidas,H,L):
    '''A funcao calcula se o colchao comprado passa pela
    porta. Digite as medidas do colchao dentro de [], da menor
    para a maior. Apos isso, digite a Altura e Largura da porta,
    respectivamente.
    #parametros | in: list (lista com as medidas do colchao, da
    menor para maior), float, float (medidas da porta) ->
    out: bool (True caso o colchao passe, False caso NAO passe.'''
    med=medidas[:2] #medidas do colchao que importam para a nossa funcao
    if med[0]<=H or med[0]<=L and med[1]<=H or med[1]<=L:
        return True
    else:
        return False