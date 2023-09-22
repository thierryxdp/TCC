def conta_frases(texto):
    """Função que dado um texto armazenado em uma string, conta o número de
       frases que aparecem neste texto, sendo cada uma delas terminada por 
       um ponto final, um ponto de exclamação, um ponto de interrogação ou 
       reticências.
       str->int
       
       Parâmetros:
       texto:O que será contado o número de frases.
       
       returns: O número de frases que aparecem no texto dado.
    """
    return str.count(texto,".","!","?","...")