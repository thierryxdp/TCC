def colchao(medidas,H,L):
    '''Função que informa se um colchao com uma determinada medida passa em um espaçp'''
    'list,int,int -> boll'
    medidas=int[medida[0],medida[1],medida[2]]
    H= int([])
    L= int([])

    dimensao={medida[0], medida[1], medida[2], H, L}

    if medida[1] <= H:
        return  True