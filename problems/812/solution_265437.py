def retira_pontuacao(frase):
    sem_pts1 = str.replace(str.replace(str.replace(str.replace(frase,',',' '),'/',' '),';',' '),':',' ')
    return sem_pts1