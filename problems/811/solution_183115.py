def colchao(medidas,H,L):
    ''' Dando como entrada uma lista 'medidas', contendo as tres dimensoes A,
    B e C de um colchao (ordenadas da menor pra maior), a altura H e a largu-
    ra L da porta, a funcao retorna se o colchao passara ou nao pela porta. 
    Todas as medidas devem ser dadas em centimetros;
    
    list, float (ou int), float (ou int) -> bool '''
    
    menor_c = medidas[0]
    media_c = medidas[1]
    maior_c = medidas[2]
    
    if (media_c <= H or media_c <= L) and (menor_c <= H or menor_c <= L):
        return True
    else: 
        return False