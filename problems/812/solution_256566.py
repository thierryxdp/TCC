def retira_pontuacao(frase):
    """..."""
    frase_filter1 = str.replace(frase,'-',' ')
    frase_filter2 = str.replace(frase_filter1,',',' ')
    frase_filter3 = str.replace(frase_filter2,'...','.')
    frase_filter4 = str.strip(o,';:.?!)
    
    return frase_filter4