def retira_pontuacao(frase):
    """ dado uma frase, retorna a frase com a pontuacao
    substituida por espaco
    str -> str"""
    trav = str.replace(frase,'-',' ')
    virgula = str.replace(trav,',',' ')
    dois_pontos = str.replace(virgula,':',' ')
    ponto_virgula = str.replace(dois_pontos,';',' ')
    ponto = str.replace(ponto_virgula,'.',' ')
    return ponto