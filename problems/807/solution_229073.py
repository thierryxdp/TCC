""" Nesta função todos os possíveis pontos que terminariam uma frase foram
transformados em apenas 1 '.', após isso foi usado o ponto final para separar
as frases entre o ponto. Porém assim a frase sempre fica com um número a mais.
str -> int
"""
def conta_frases(frase):
    f1 = frase.replace('...', '.')
    f2 = f1.replace('!', '.')
    f3 = f2.replace('?', '.')
    f4 = f3.split('.')
    return len(f4) - 1