def colchao(medidas,H,L):
    'Função que diz se um colchão passa por uma porta, dada as medidas da porta e do colchão'
    'list/int/int -> Bool'
    return medidas[1] <= H or medidas[2] <= L