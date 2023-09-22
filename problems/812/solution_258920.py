def retira_pontuacao(frase):
    
    sem_pontos1=str.replace(frase,"-"," ")
    sem_pontos2=str.replace(sem_pontos1,","," ")
    sem_pontos3=str.replace(sem_pontos2,":"," ")
    sem_pontos4=str.replace(sem_pontos3,";"," ")
    sem_pontos5=str.replace(sem_pontos4,"."," ")
    
    return sem_pontos5