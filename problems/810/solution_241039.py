def inverte(texto):
    #Retirar pontuação
    sem_pont = texto
    sem_pont = sem_pont.replace("...",)
    sem_pont = sem_pont.replace(".",)
    sem_pont = sem_pont.replace(",",)
    sem_pont = sem_pont.replace("?",)
    sem_pont = sem_pont.replace("!",)
    sem_pont = sem_pont.replace("-",)
    sem_pont = sem_pont.replace(";",)
    #inverter a ordem
    frase_final = sem_pont
    return frase_final[::-1]