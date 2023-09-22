def total (compras,dic):
    '''
       Função que recebe uma lista de compras (compras) e um
       dicionário (dic) contendo o preço de cada produto 
       disónível e retorna o valor total dos intens da lista
       que estejam disponíveis na loja;
       list, dict -> int
    '''
    valor=0
    for item in compras:
        if item in dic:
            valor += dict.get(dic,item)
    return round(valor, 2)