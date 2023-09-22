def conta_frases(texto):
    """Uma função que retorna a quantidade de frases presentes em um texto
considerando que uma frase termina em ".","?","..." ou "!". Esses pontos devem aparecer
somento no final de cada frase. String; String->int"""
    texto2=texto.split()
    Quant_pontos_finais=texto2.count(".")
    Quant_pontos_interrog=texto2.count("?")
    Quant_pontos_exclam=texto2.count("!")
    Quant_pontos_ret=texto2.count("...")
    return Quant_pontos_ret + Quant_pontos_exclam + Quant_pontos_interrog +Quant_pontos_finais