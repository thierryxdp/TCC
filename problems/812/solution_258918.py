def retira_pontuacao(frase: str) -> str:
    '''dada uma frase, retira todas as pontuações dela'''
    sem_pont = str.replace(frase, "_", " ")
    sem_pont = str.replace(sem_pont, ",", " ")
    sem_pont = str.replace(sem_pont, ";", " ")
    sem_pont = str.replace(sem_pont, ":", " ")
    sem_pont = str.replace(sem_pont, ".", " ")
    sem_pont = str.replace(sem_pont, "?", " ")
    sem_pont = str.replace(sem_pont, "!", " ")
    sem_pont = str.replace(sem_pont, "-", " ")
    
    return sem_pont