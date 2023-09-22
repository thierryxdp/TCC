def retira_pontuacao(frase: str) -> str:
    sem_pont = ""
    i = 0
    
    while (i < len(frase)):
        if (frase[i] in "-,:;.!?"):
            sem_pont += " "
        else:
            sem_pont += frase[i]
    
    return sem_pont