def conta_frases(texto):
    subs_reticencias = str.replace(texto, '...', '/')
    subs_exclamacao = str.replace(subs_reticencias, '!', '/')
    subs_interrogacao = str.replace(subs_exclamacao, '?', '/')
    subs_ponto = str.replace(subs_interrogacao, '.', '/')
    return str.count(subs_ponto, '/')