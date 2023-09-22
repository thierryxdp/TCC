def retira_pontuacao(frase):
    """dada uma frase, a mesma é retornada sem suas pontuações
    string-->string"""
    d={,":" ",".":" ","!":" ","?":" ",":":" ",";":" ","-":" "}
    for c in d:
       frase=str.replace(frase,c,d[c])
    return frase