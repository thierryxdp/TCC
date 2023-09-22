def retira_pontuacao(f):
    """"""
    sem_trav = str.replace(f, '-', ' ')
    sem_vir = str.replace(f, ',', ' ')
    sem_2p = str.replace(f, ':', ' ')
    sem_pvir = str.replace(f, ';', ' ')
    sem_ponto = str.replace(f, '.', ' ')
    sem_exc = str.replace(f, '!', ' ')
    sem_int = str.replace(f, '?', ' ')
    if '...' in f:
        sem_ret = str.replace(f, '...', '.')
        sem_ponto = str.replace(sem_ret, '.', ' ')
    return f