def retira_pontuacao(frase):
    """A funcao retira toda pontuacao da frase dada como entrada; str=>str"""
    frase1= frase.repleace(frase,',',' ')
    frase2= frase1.repleace(frase1,'-',' ')
    frase3= frase2.repleace(frase2,':',' ')
    frase4= frase3.repleace(frase2,';',' ')
    return frase4