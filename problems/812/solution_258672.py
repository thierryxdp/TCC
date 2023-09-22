def retira_pontuacao(texto):
    """funcao que dada uma frase, retorna a frase com todos os pontos substituidos por espaco"""
    """str->str"""
    ponto=str.replace(texto,'.',' ')
    reticencias=str.count(texto,'...',' ')
    interrogacao=str.count(texto,'?',' ')
    exclamacao=str.count(texto,'!',' ')