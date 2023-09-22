def retira_pontuacao(frase):
    sem_pts1 = frase.replace(frase.replace(frase.replace('/',''),':',''),',','')
    sem_pts2 = sem_pts1.replace(sem_pts1.replace(';',''),'.','')
    return sem_pts2