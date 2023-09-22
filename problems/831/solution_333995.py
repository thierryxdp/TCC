def lingua_p(string):
    '''Dada uma string retornar a mesma com 'p' após cada vogal 
    str -> str'''
    traducao = ''
    string.lower()
    s = list(string)
    for i in range(len(s)):
        if s[i] in 'aáàãâeéèêiíìîoóòõuôúùû':
            traducao += s[i]
            traducao += 'p'
            traducao += s[i]
        else:
            traducao += s[i]
    return traducao