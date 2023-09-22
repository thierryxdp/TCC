def colchao(medidas,H,L):
    '''Função que informa se um colchao com uma determinada medida passa em um espaçp'''
    'list,int,int -> boll'
    medidas=[medidas[0],medidas[1],medidas[2]]
    H=int()
    L=int()
    medidas[0]=int()
    medidas[1]=int()
    medidas[2]=int()
    if  L < medidas[2]:
        return  True