def hashtag(s):
    """recebe uma string e adiciona '#' no 
    início, meio e final dela. entrada e 
    saída: str"""
    return s[:0]+'#'+s[:((len(s))//2)+1]+'#'+s[len(s)//2:]+'#'