def conta_frases(texto):
    """Retorna a quantidade de frases que aparecem no texto que é o parâmetro de entrada;
    str->int"""
    return texto.count(.)+texto.count(!)+texto.count(?)-2*(texto.count(...))