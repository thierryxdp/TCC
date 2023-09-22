def conta_frases(texto):
    "Retorne o numero de frases de um dado texto; str->int"
    return str.count(texto,'.'and'...'and'!'and'?')