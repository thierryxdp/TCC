def colchao(medidas,H,L):
    '''Função que calcula e retorna se será possível passar o
    colchão pela porta.
    entrada da funçao: lista e dois int
    saída da função: bool'''
    medidas.sort()
    
    altura = medidas[0]
    largura = medidas[1]
    comprimento = medidas[2]
   
    if comprimento < H:
        return True
    
    if largura < altura:
        return True
    
    if largura < L:
        return True
    
    return False