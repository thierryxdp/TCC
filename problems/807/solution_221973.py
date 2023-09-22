def conta_frases(texto):
    """Recebe um texto e retorna a quantidade de frases
    contidada nesse texto
    str - > int """
    reticencias = str.replace(texto,'...','¬')
    ponto = str.replace(reticencias,'.','¬')
    exclamacao = str.replace(ponto,'!','¬')
    interrogacao = str.replace(exclamacao,'?','¬')
    novo = str.split(interrogacao,'¬')
    qtd = len(novo)-1
    return qtd