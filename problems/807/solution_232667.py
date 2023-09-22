def conta_frases(texto):
  '''Função que retorna a quantidade de frases de um texto. str -> int'''
    ponto = texto.count(".")
    interrogacao = texto.count("!")
    exclamacao = texto.count("?")
    reticencias = texto.count("...")
    frasecomreticencias = (reticencias*3)
    if "..." in texto:
        return (ponto+interrogacao+exclamacao+reticencias-frasecomreticencias)
    else:
        return (ponto+interrogacao+exclamacao)