def retira_pontuacao(frase):
    """..."""
    frase_filter1 = str.replace(frase,'-',' ')
    frase_filter2 = str.replace(frase_filter1,',',' ')
    frase_filter3 = str.replace(frase_filter2,'...','.')
    frase_filter4 = str.replace(frase_filter3,'.',' ')
    frase_filter5 = str.replace(frase_filter4,';',' ')
    frase_filter6 = str.replace(frase_filter5,':',' ')
    frase_filter7 = str.replace(frase_filter6,'!',' ')
    frase_filter8 = str.replace(frase_filter7,'?',' ')
    
    return frase_filter8