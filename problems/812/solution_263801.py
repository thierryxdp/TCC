def retira_pontuacao(frase):
    frase_sem_pontuacao=frase.replace('-',' ').replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ')
    return frase_sem_pontuacao