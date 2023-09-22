def maiores(minha_lista,n):
    maior_que = n
    filtrados = [x for x in minha_lista if x > maior_que]
    return sorted(filtrados)