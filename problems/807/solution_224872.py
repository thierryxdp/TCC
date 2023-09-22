def conta_frases(texto):
    """essa função, dado um texto(igual ao parâmetro de entrada texto) armazenado em 
uma string, retorna o número de frases que aparecem nesse texto.Cada frase no texto é
terminada com um ponto final, um ponto de exclamação, um ponto
de interrogação ou 3 pontos em sequência(reticências)
string->int"""
    nReticencias= str.count(texto,'...')
    nPontoFinal= str.count(texto, '.') - 3*nReticencias
    return nReticencias + nPontoFinal + str.count(texto, '!') + str.count(texto, '?')