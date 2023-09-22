def retira_pontuacao(texto):
    """Retira toda pontuação do texto; str==> str"""
    
    resp= texto.translate(str.maketrans('', '', string.punctuation))
    return resp