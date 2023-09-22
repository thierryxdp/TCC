def inverte(s):
    """
    Retorna a string informada com as palavras em ordem invertida
    Parametros:
    	s -> str
        String a ser manipulada
    Returns:
    	str
        string invertida
    """
    sem_ponto=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(s,"-"," "),","," "),":"," "),";"," "),"."," "),"?"," "),"!"," ")
    minuscula=str.lower(sem_ponto)
    palavras=str.split(minuscula)
    inverso=list.reverse(palavras)
    return inverso