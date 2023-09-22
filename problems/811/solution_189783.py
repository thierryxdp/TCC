def colchao(medidas, H, L):
    '''Função que dada as medidas de um colchão, e a medida de um porta, retorna se
    o colchão passaria por essa  porta ou não.
    param medidas -> list[menor_medida, medida, maior_medida]
    param H -> int
    param L -> int'''
    
    altura, largura, comprimento = medidas
    
    if largura <= L:
        return True
    
    if comprimento > H:
        
        if largura <= H:
            return True
        if largura > H:
            return False