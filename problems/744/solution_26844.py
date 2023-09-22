def hashtag(s):
    """funcao que insere uma # no inicio, no meio e no final de uma string s;
    str -> str"""
    
    meio = len(s)/2
    meioFinal = int(meio) 
    
    return '#' + s[0:meioFinal] + '#' + s[meioFinal:] + '#'