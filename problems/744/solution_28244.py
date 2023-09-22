def hashtag(string):
    """retorna a string da entrada com # no meio e # no fim da string
    str->str"""
    string = "#" + string[:len(string)//2] + "#" + string[len(string)//2:] + "#"
    return string