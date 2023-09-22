def retira_pontuacao(frase):
    """dada uma frase, a mesma é retornada sem suas pontuações
    string-->string"""
    L=[".",",","!","?",";",":","-","..."]     
    for c in L:
    return str.replace(frase,c," ")