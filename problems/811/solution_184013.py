def colchao(medidas,H,L):
    '''Retorna True se o colchão passa pelas
       portas e False se o colchão não passa;
       Insira uma lista com as medidas do colchão,
       da menor para a maior e em cm;
       list,int,int->bool'''
    if medidas[1]<=H:
        return True
    else:
        return False