def conta_frase (texto):
    novo_texto = str.replace(texto,"..." , ".")
    ponto_final = str.count(novo_texto, "." , 0 , len(texto))
    ponto_exclamacao = str.count(novo_texto, "!" , 0 , len(texto))
    ponoto_interrogacao = str.count(novo_texto, "?", 0 , len(texto))
    return ponto_final+ponto_eclamacao+ponto_interrogacao