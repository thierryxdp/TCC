def retira_pontuacao(frase):
    """A funcao retira toda pontuacao da frase dada como entrada; str=>str"""
    frase1= str.repleace(frase,',',' ')
    frase2= str.repleace(frase1,'-',' ')
    frase3= str.repleace(frase2,':',' ')
    frase4= str.repleace(frase2,';',' ')
    return frase4