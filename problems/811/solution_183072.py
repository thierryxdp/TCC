def colchao(medidas,H,L):
    '''Função que determina se o colchão comprado por João, passa(se a função retornar True) ou não(se a função retornar False) pela porta de sua casa.
       parâmetros de entrada: list,int, int
       valor de retorno:bool'''
    if medidas[1]<=H:
        return True
    else:
        return False