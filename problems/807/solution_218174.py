def conta_frases(texto):
    """Retorna a quantidade de frases que aparecem no texto que é o parâmetro de entrada;
    str->int"""
    a=texto
    return a.count('.')+a.count('!')+a.count('?')-2*(a.count('...'))