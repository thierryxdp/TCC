def retira_pontuacao(frase:str)->list:
    """funcao que retorna a frase sem nenhuma pontuacao"""
    
    sem_pontos1=str.replace(frase,"-"," ")
    sem_pontos2=str.replace(sem_pontos1,","," ")
    sem_pontos3=str.replace(sem_pontos2,":"," ")
    sem_pontos4=str.replace(sem_pontos3,";"," ")
    sem_pontos5=str.replace(sem_pontos4,"."," ")
    sem_pontos6=str.replace(sem_pontos5,"!"," ")
    sem_pontos7=str.replace(sem_pontos6,"?"," ")
    
    return sem_pontos7