def retira_pontuacao(texto):
    """Função que retorna a frase sem os caracteres de pontuação.
    str->str"""
    if ',' in texto:
        return del str.find(texto,',')
    else:
        texto