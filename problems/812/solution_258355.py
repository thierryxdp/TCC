def retira_pontuacao(frase):
    """A funcao retira toda pontuacao da frase dada como entrada; str=>str"""
    frase1= frase.replace(frase,',',' ')
    frase2= frase1.replace(frase1,'-',' ')
    frase3= frase2.replace(frase2,':',' ')
    frase4= frase3.replace(frase2,';',' ')
    return frase4