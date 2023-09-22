def conta_frases(texto):
    """Uma função que retorna a quantidade de frases presentes em um texto
considerando que uma frase termina em ".","?","..." ou "!". Esses pontos devem aparecer
somento no final de cada frase. String; String->int"""
    Quant_pontos_finais=texto.count(".")
    Quant_pontos_interrog=texto.count("?")
    Quant_pontos_exclam=texto.count("!")
    Quant_pontos_ret=texto.count("...")
    return Quant_pontos_ret + Quant_pontos_exclam + Quant_pontos_interrog +Quant_pontos_finais