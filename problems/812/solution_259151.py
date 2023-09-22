def retira_pontuacao(frase):
    """Substitui toda pontuação da frase por espaços;
    str -> str"""
    sem_pont = str.replace(frase, "-", " ")
    sem_pont = str.replace(frase,"," ," ")
    sem_pont = str.replace(frase,";" ," ")
    sem_pont = str.replace(frase,"." ," ")
    sem_pont = str.replace(frase,"!" ," ")
    sem_pont = str.replace(frase,"..." ," ")
    sem_pont = str.replace(frase,"?" ," ")
    return sem_pont