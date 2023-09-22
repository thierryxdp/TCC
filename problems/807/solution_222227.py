def conta_frases(texto):
    """ Conta o número de frases que aparecem no texto (texto). Cada frase é terminada com um ponto final (.), um ponto de exclamaçã9 (!),
    de interrogação (?), ou reticências (...). Pontos de exclamação ou interrogação não devem aparecer em sequência no texto 
    e só devem aparecer terminando uma frase 
    str -> int """
    return texto.count('...')*-2+texto.count('.')+texto.count('!')+texto.count('?')