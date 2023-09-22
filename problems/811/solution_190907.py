def colchao(medidas, H, L):
    '''a funcao retorna se o colchao passa pela porta, dado as medidas do colchao
    ordenada da menor para a maior. H corresponde a altura da porta e L a largura
    list[int], int, int -> bool'''
    area1=medidas[1]*medidas[2]
    area2=medidas[0]*medidas[2]
    area3=medidas[0]*medidas[1]
    if area1<H*L or area2<H*L or area3<H*L:
        return 'True'
    return 'False'