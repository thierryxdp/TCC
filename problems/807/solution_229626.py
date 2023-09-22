def conta_frases(texto)
"""Função que, dado um texto, retorna o número de frases que aparecem neste texto.
str -> int"""
exclamacao = str.count(texto, "!")
interrogacao = str.count(texto, "?")
ponto = str.count(texto, ".")
reticencias = str.count(texto, "...")
return exclamacao + interrogacao + ponto + reticencias