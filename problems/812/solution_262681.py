def retira_pontuacao(f):
    """"""
    sem_trav = str.replace(f, '-', ' ')
    sem_vir = str.replace(f, ',', ' ')
    sem_2p = str.replace(f, ':', ' ')
    sem_pvir = str.replace(f, ';', ' ')
    sem_ponto = str.replace(f, '.', ' ')
    sem_exc = str.replace(f, '!', ' ')
    sem_int = str.replace(f, '?', ' ')
    novo = sem_trav + sem_vir + sem_2p + sem_pvir + sem_ponto + sem_exc + sem_int
    if '...' in f:
        sem_ret = str.replace(f, '...', '.')
        sem_ponto = str.replace(sem_ret, '.', ' ')
    return novo