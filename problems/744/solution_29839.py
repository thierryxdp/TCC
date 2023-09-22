def hashtag(s):
    """ Recebe uma string e insere o caractere # no inicio, no meio e no seu fim. 
    str -> str """
    return "#"+s[:len(s)//2]+"#"+s[len(s)//2:]+"#"