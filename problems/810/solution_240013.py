def retira_pontuacao(frase: str) -> str:
    sem_pont = str.replace(frase, "-", " ")
    sem_pont = str.replace(sem_pont, ",", " ")
    sem_pont = str.replace(sem_pont, ":", " ")
    sem_pont = str.replace(sem_pont, ";", " ")
    sem_pont = str.replace(sem_pont, ".", " ")
    sem_pont = str.replace(sem_pont, "?", " ")
    sem_pont = str.replace(sem_pont, "!", " ")
    
    return sem_pont

def inverte(frase: str) -> str:
    sem_pont = retira_pontuacao(frase)
    palavras = str.split(sem_pont)
    invertidas = palavras[::-1]
    
    return str.join(" ", invertidas)