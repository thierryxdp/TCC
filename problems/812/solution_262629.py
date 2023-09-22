def retira_pontuacao(frase):
    """Função que dada frase, a retorna com suas pontuações substituídas por espaço;
    str -> str"""
    if (',') in frase == True and ('-','-',';',':','.') in frase == False:
        return (frase.replace(',',' '))