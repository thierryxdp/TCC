def retira_pontuacao(frase):
    """
    Função que dada uma frase retorna a frase onde todos os caracteres de pontuação foram substituídos por espaço
    str-> str
    
    Parameters:
    frase: Parâmetro do tipo str que representa a frase inserida
    """
     nfrase = frase[:]
    for caractere in ["-", ",", ":", ";" , ".", "!", "?", "..."]:
        nfrase = str.replace(nfrase, caractere, " ")
    return nfrase