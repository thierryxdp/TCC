def retira_pontuacao(frase):
    """Funcao que, dada uma frase, retorna ela sendo que todos os caracteres de pontuacao tenham sido substituidos por espaco
       str-> str"""
    
    frase2=frase[:]
    for caractere in ["-", ",", ":", ";", ".", "!", "?", "..."]:
        frase2=str.replace(frase2, caractere, " ")
        return frase2