def conta_frases(texto):
"""função que conta os numeros das frases que aparecem no texto acima.
entrada:str
saida:int"""

novotexto=str.replace(texto,"...",".")
ponto=str.count(novotexto,".",0,len(texto))
exclamacao=str.count(novotexto,"!",0,len(texto))
interrogacao=str.count(novotexto,"?",0,len(texto))
    return ponto+exclamacao+interrogacao