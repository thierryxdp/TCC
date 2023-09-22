import re
def conta_frase(frase):
 frase1 = frase.replace("...", "." )
 frase2 = frase1.replace("!",".")
 frase3 = frase2.replace("?",".")
 frase4 = frase3.replace(";",".")
 frase5 = frase4.split(".")
 n = len(frase5)
 return n