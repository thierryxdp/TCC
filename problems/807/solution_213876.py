def conta_frases(paragrafo):
    """Recebe um conjunto de sentenças e conta quantas frases estão presentes
    na string"""
    paragrafo_novo = paragrafo_novo.replace('?', '.')
    paragrafo_novo = paragrafo_novo.replace('!', '.')
    paragrafo_novo = paragrafo_novo.replace('...', '.')   
    paragrafo_novo = paragrafo_novo.split('.')
    return len(paragrafo_novo)