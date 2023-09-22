def conta_frases(texto):
    '''Recebe um texto e retorna o número de frases desse texto.
    Cada frase é terminada com um ponto final, um ponto de exclamação,
    um ponto de interrogação ou reticências.
    Obs: Pontos de exclamação e interrogação não aparecem repetidos e
    só aparecem no texto terminando uma frase.
    
    str -> int

    Explicação: troca as reticências, os pontos de exclamacão e os
    pontos de interrogação por ponto finais, divide as frases usando
    como referência os pontos finais e, por fim, conta quantas frases
    são (subtraindo 1, porque sempre irá ter um espaço em branco no
    fim da lista das frases)'''

    texto = str.replace(texto, "...", ".")
    texto = str.replace(texto, "!", ".")
    texto = str.replace(texto, "?", ".")

    frases = str.split(texto, ".")
    numeroFrases = len(frases) - 1

    return numeroFrases