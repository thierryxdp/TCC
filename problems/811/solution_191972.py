def colchao(medidas,H,L):

    '''funcao que descobre se o colchão passa pelas portas da casa e retorna essa resposta.
    entrada:lista e 2int;
    saida: ferramenta bool'''
   
    medidas.sort()
    
    altura_colchao=medidas[0]
    largura_colchao=medidas[1]
    comprimento_colchao=medidas[2]

    if comprimento_colchao<H:
        return True
    if largura_colchao<H:
        return True
    if largura_colchao<L:
        return True
    else:
        return False