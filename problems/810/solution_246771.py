def inverter(txt):
    """função que inverte a ordem das palavras e remove sua pontuação
  	str->str"""
    frase=txt
    inversa= ' '.join(reversed(txt))
    return inversa