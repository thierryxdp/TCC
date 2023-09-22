def hashtag(s):
    '''dada uma string s, insere uma hashtag no comeco, meio e fim dela
    str -> str'''
    meio = len(s) // 2
    return '#' + s[:meio] + '#' + s[meio:] + '#'