def conta_frases(texto):
    ponto = str.replace(texto,'.','¬')
    exclamacao = str.replace(ponto,'!','¬')
    interrogacao = str.replace(exclamacao,'?','¬')
    reticencias = str.replace(interrogacao,'...','¬')
    novo = str.split(reticencias,'¬')
    qtd = len(novo)
    return qtd