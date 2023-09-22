def maiores(minha_lista,n):
    '''Retorna a lista ordenada com as notas acima da media
    float,int-->float'''
    maior_que = n
    filtrados = [x for x in minha_lista if x > maior_que]
    return sorted(filtrados)