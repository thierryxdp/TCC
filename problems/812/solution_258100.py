def retira_pontuacao(frase):
    """Substitui todas as pontuacoes da frase fornecida por espaços vazios;
    str -> str"""
    ponto = ["!", "?"]
    v1 = str.split(frase, ponto)
    v2 = str.join(" ", v1)
    
    return v2