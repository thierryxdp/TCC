def conta_frases(texto):
     """função que contao numero de frases que aparecemno texto.cada frase no texto
     é terminada com um ponto final,um ponto de exclamação, um ponto de interrrogação
     ou reticencias. Pontos de exclamação ou de interrogação não aparecem repitidos em
     sequencia no texto e esses simbolossó aparecem notexto terminado da frase.
     str -> int
     """

     invert_txt= str.replace(str.replace((texto.replace('?','.')),'...','.'),'!','.')

     return len(invert_txt.split('.'))-1