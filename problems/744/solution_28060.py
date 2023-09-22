def hashtag(s):
    """Função que receba uma string(s) e insira o carectere "#" no início, no meio
    e no final dela.
    string -> string"""
    return ('#' + s[0:(len(s)//2)] + '#' + s[(len(s)//2):(len(s))] + '#')