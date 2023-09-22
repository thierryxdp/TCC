def inverte(frase):
    """ Retorna a frase a invertendo e substituindo seus caracteres de pontuação por espaço, string -> string """ 
    sem_final = str.replace(frase,"."," ");
    sem_exclamacao = str.replace(sem_final,"!"," ");
    sem_interrogacao = str.replace(sem_exclamacao,"?"," ");
    sem_reticencias = str.replace(sem_interrogacao,"..."," ");
    sem_travesssao = str.replace(sem_reticencias,"-"," ");
    sem_virgula = str.replace(sem_travesssao,","," ");
    sem_dois_pontos = str.replace(sem_virgula,":"," ");
    sem_ponto_virgula = str.replace(sem_dois_pontos,";"," ");
    lista = str.split(sem_ponto_virgula);
    inverso = lista[::-1];
    return str.join(" ",inverso);