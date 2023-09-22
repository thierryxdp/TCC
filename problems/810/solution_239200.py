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

def inverte(frase:str) -> str:
    """Dada uma frase, retorna uma outra frase com as mesmas palavras
    na ordem inversa,sem pontuação e com letras minúsculas"""
    frase_sem_pontuacao = retira_pontuacao(frase)
    frase_sem_pontuacao_minuscula = str.lower(frase_sem_pontuacao)
    frase_separada = str.split(frase_sem_pontuacao_minuscula,' ')
    frase_invertida = str.join(' ',frase_separada[::-1])
    return frase_invertida