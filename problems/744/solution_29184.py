def hashtag(s):
    """recebe uma string s e coloca a string # no começo, 
    no meio e no final da string s"""
    A = str('#')
    B = s[0:(len(s)//2)]
    C = s[(len(s)//2):]
    return A + B + A + C + A