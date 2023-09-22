def total(compra,preco):
    '''
    A função recebe duas variaveis, uma lista de compras e
    um dicionario com o preço dos itens e retorna o preço dos
    itens que estão na lista
    '''
    
    itens= 0
    total= 0
    while itens< len(compra):
         if compra[itens] in preco:
            dinheiro= dict.get(preco,compra[itens])
            total= total + dinheiro
            itens+= 1
        
    return round(total,2)