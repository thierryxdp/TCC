def retira_pontuacao(frase):
    sem_pts1 = str.replace(str.replace(str.replace(str.replace(frase,',',' '),'/',' '),';',' '),':',' ')
    return str.replace(sem_pts1,'.',' ')