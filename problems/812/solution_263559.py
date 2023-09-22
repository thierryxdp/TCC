def retira_pontuacao(texto):
    """Função que retorna a frase sem os caracteres de pontuação.
    str->str"""
    if ',' in texto:
        a=str.find(texto,',')
        del texto[a] 
        return texto
    else:
        texto