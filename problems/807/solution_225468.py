def conta_frases(texto):
    subs_pontos = str.replace(texto,'.','-')
    subs_exclamacao = str.replace(subs_pontos,'!','-')
    subs_interrogacao = str.replace(subs_interrogacao,'?','-')
    return str.count(subs_interrogacao,'-')+1