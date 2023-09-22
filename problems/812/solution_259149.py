def retira_pontuacao(frase: str) -> str:
    sem_pont = str.replace(frase, "-", " ")
    sem_pont = str.replace(sem_pont, ",", " ")
    sem_pont = str.replace(sem_pont, ":", " ")
    sem_pont = str.replace(sem_pont, ";", " ")
    sem_pont = str.replace(sem_pont, ".", " ")
    sem_pont = str.replace(sem_pont, "!", " ")
    sem_pont = str.replace(sem_pont, "?", " ")
    sem_pont = str.replace(sem_pont, "...", " ")
    
    return sem_pont