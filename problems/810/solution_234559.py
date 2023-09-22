def inverte(frase):
'''sasa uma frase retorna essa frasw na ordem inversa, sem inverter as palavras
sting -> string'''
frase1  str.replace(texto, "-", " ")
frase2 = str.replace(frase1, ",", " ")
frase3 = str.replace(frase2, "...", " ")
frase4 = str.replace(frase3, "..", " ")
frase5 = str.replace(frase4, ";". " ")
frase6 = str.replace(frase5, "!", " ")
frase7 = str.replace(frase6, "?", " ")
frase minuscula = str.lower(frase7)
frase nova = str.split(frase minuscula, " ")
frase nova2 = frase_nova[::-1]
string = " ".join(frase_nova)
return string