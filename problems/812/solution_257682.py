def retira_pontuacao(frase):
    """" retira a pontução das frases;str->str"""
    return str.split(frase,",") or str.split(frase,"!")