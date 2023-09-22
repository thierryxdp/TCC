def hashtag(s)
"""Função que recebe uma string s como entrada e insere o caracter "#' no ínicio,
no meio e no final d string:
string -> string"""

stringEntrada= string(s)
compriento= len(s)
razao= comprimento//2
stringHashtang= '#' = stringEntrada [:razao]
+ '#' +stringEntrada[razao:] +'#'
return stringHanstag