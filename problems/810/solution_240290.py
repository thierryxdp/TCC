def retira_pontuacao(frase):
    """Substitui toda pontuação da frase por espaços;
    str -> str"""
    sem_pont = str.replace(frase, "-", " ")
    sem_pont = str.replace(sem_pont,", " ," ")
    sem_pont = str.replace(sem_pont,";" ," ")
    sem_pont = str.replace(sem_pont,"." ," ")
    sem_pont = str.replace(sem_pont,"!" ," ")
    sem_pont = str.replace(sem_pont,"..." ," ")
    sem_pont = str.replace(sem_pont,"?" ," ")
    return sem_pont

def inverte(frase):
    lista= str.split(str.lower(retira_pontuacao(frase)), " ")
    return str.strip(str.join(" ", lista[-1::-1]), " ")