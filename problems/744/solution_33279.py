def hashtag(s):
    """retorne a string de entrada com o formato de #no início, no meio e no final da string"""
     s = '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'
     return s