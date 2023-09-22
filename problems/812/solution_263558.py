def retira_pontuacao(texto):
    """Função que retorna a frase sem os caracteres de pontuação.
    str->str"""
    if ',' in texto:
        del str.find(texto,',')
        return texto
    else:
        texto