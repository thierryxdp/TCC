def conta_frases ( texto ):
    """Funcao que recebe um texto e retorna o numero de frases nesse texto .Eh considerado que cada frase no texto termina com um ponto final , um ponto de exclamacao , um ponto de interrogacao ou tres pontos
em sequencia ( reticencias ).
str -> int"""
    texto = str . count ( texto= "... ,//" )
texto = str . count ( texto= "., // ")
texto = str . count ( texto =  "!,// ")
texto = str . count ( texto= "? ,  // ")
   return len  (texto.split ("// "))