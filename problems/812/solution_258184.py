def retira_pontuacao(frase : str)->str:
    """Dada uma frase, retorna essa frase sem os caracteres
    de pontuação."""
    frase_limpa = str.replace(str.replace(str.replace
    (str.replace(str.replace(str.replace
    (str.replace(frase,'.',' '),',',' '),';',' ')
                 ,':',' '),'-',' '),'?',' '),'!',' ')
    return frase_limpa