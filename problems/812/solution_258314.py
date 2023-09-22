def retira_pontuacao(frase:str)-> str:
    """Dada uma frase, retorna a mesma frase sem sua pontuação"""
    frase_sem_travessao = str.replace(frase,'-',' ')
    frase_sem_virgula = str.replace(frase_sem_travessao,',',' ')
    frase_sem_doispontos = str.replace(frase_sem_virgula,':',' ')
    frase_sem_pontovirgula = str.replace(frase_sem_doispontos,';',' ')
    frase_sem_exclamacao = str.replace(frase_sem_pontovirgula,'!',' ')
    frase_sem_interrogacao = str.replace(frase_sem_exclamacao,'?',' ')
    frase_sem_ponto = str.replace(frase_sem_interrogacao,'.',' ')
    return frase_sem_ponto