def colchao(medidas,H,L):
    '''Retorna True se o colchão passa pelas
       portas e False se o colchão não passa;
       Insira uma lista com as medidas do colchão,
       da menor para a maior e em cm;
       list,int,int->bool'''
    porta=H*L
    colchao=2*(medidas[0]*medidas[1]+medidas[0]*medidas[2]+medidas[1]*medidas[2])
    if porta>=colchao:
        return True
    if colchao>porta:
        return False