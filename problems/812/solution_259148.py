def retira_pontuacao(frase):
    """Substitui toda pontuação da frase por espaços;
    str -> str"""
    sem_pont = str.replace("-", "")
    sem_pont = str.replace("," ,"")
    sem_pont = str.replace(";" ,"")
    sem_pont = str.replace("." ,"")
    sem_pont = str.replace("!" ,"")
    sem_pont = str.replace("..." ,"")
    sem_pont = str.replace("?" ,"")
    return sem_pont