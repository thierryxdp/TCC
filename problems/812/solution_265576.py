def retira_pontuacao(frase):
    """dada uma frase, a mesma é retornada sem suas pontuações
    string-->string"""
    L=[".",",","!","?",";",":","-","..."]     
    for c in L:
       frase=str.replace(frase,c," ")
    return frase