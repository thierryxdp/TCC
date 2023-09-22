def conta_frases(s):
    """
    Informa quantas frases tem em uma string
    Parametros:
    	s -> str
        string a ser analisada
    Returns:
    	int
        nunmero de frases
    """
    pontos=str.replace(str.replace(str.replace(s,"...","."),"!","."),"?",".")
    n=str.split(pontos,".")
    if n[len(n)-1]=="":
        return len(n)-1
    else:
        return len(n)