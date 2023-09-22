def hashtag(s):
    """retorne a string de entrada com o formato de #no início, no meio e no final da string"""
     str(s) = '#' + str(s)[:len(s)//2] + '#' + str(s)[len(s)//2:] + '#'
     return s