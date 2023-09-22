def retira_pontuacao(frase):
    """Substitui todas as pontuacoes da frase fornecida por espaços vazios;
    str -> str"""
    ponto = ["!", "?", ",", ".", "-", ":", ";"]
    F= str.replace(frase, ponto, " ")
    
    return F