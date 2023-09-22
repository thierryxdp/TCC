def lingua_p(s):
    '''
    Esta função recebe uma string e retorna outra string baseada na string original, onde todas as vogais são
    seguidas da letra 'p' e delas mesmas.
    
    Parametros
    ----------
    s (str) : string
    '''
    s = [c for c in s]
    v = ['a', 'e', 'i', 'o', 'u', 'é', 'á', 'à', 'í', 'ú', 'ó']
    for i in range(len(s)):
        if s[i].lower() in v:
            s[i] = s[i] + 'p' + s[i]
    return ''.join(s)