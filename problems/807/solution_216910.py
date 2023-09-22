def conta_frases(texto):
    '''A partir de um texto retorna o numero de frases. Cada frase deve ser
    finalizada por um ponto, tres pontos, interrogacao ou exclamacao
    string -> int'''
    sem_int = str.replace(texto,'?','.')
    so_ponto = str.replace(sem_int,'!','.')
    return int(str.count(so_ponto,'. '))+1