def conta_frases(texto):
    '''Coloque um texto em string e o resultado será o número de frases deste texto, usando como crtérios os pontos de exclamação, pontos de interrogação ou três pontos em sequência'''
    Quant_pontos_finais=texto.count(".")
    Quant_pontos_interrog=texto.count("?")
    Quant_pontos_exclam=texto.count("!")
    Quant_pontos_ret=texto.count("...")
    return Quant_pontos_ret-3*Quant_pontos_ret+Quant_pontos_exclam+Quant_pontos_interrog+Quant_pontos_finais