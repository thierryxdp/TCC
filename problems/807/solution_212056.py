def conta_frases(string):
    """Retorna o número de frases no texto; string -> int."""
    string = str.replace(string,".","#")
    string = str.replace(string,"...","#")
    string = str.replace(string,"!","#")
    string = str.replace(string,"?","#")
    return len(str.split(string,"#"))