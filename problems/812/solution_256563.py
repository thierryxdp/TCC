def retira_pontuacao(frase):
    """..."""
    retira_final_inicial = str.strip(frase,'?!.:;')
    frase_filter1 = str.replace(retira_final_inicial,'-',' ')
    frase_filter2 = str.replace(frase_filter1,',',' ')
    
    return frase_filter2