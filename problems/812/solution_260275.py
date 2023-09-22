def retira_pontuacao(frase):
    sem_pontos = frase.replace('...', ' ').replace('.', ' ').replace('!', ' ')
    sem_pontos = sem_pontos.replace('?', ' ').replace('-', ' ').replace(';', ' ')
    return sem_pontos