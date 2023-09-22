def retira_pontuacao(frase):
    """ Retorna a frase substituindo seus caracteres de pontuação por espaço, string -> string """ 
    sem_final = str.replace(frase,"."," ");
    sem_exclamação = str.replace(sem_final,"!"," ");
    sem_interrogacao = str.replace(sem_exclamação,"?"," ");
    sem_reticencias = str.replace(sem_interrogacao,"..."," ");
    sem_travesssao = str.replace(sem_reticencias,"-"," ");
    sem_virgula = str.replace(sem_travesssao,","," ");
    sem_dois_pontos = str.replace(sem_virgula,":"," ");
    sem_ponto_virgula = str.replace(sem_dois_pontos,";"," ");
    return sem_ponto_virgula;