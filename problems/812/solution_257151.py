def retira_pontuacao(texto):
    """Função que recebe um texto e substitui todas as pontuaçôes por espaço
       Parametros: str -> str"""
    pontos = ['!','?','.',',',':']
    for substituir in pontos:
        texto = texto.replace(substituir,' ')
    return texto