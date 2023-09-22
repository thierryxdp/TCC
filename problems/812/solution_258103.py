def retira_pontuacao(frase):
    """Substitui todas as pontuacoes da frase fornecida por espaços vazios;
    str -> str"""
    
    ve = str.split(frase, "!")
    v1 = str.join(" ", ve)
    vi = str.split(frase, "?")
    v2 = str.join(" ", vi)
    return v1, v2