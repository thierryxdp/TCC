def hashtag(s):
    '''Funçap que dado uma string na entrada retorna com o 
    caractere ''#''
    Entrada: String
    Saida String'''
    s=len(s)//2
    return '#' + s[:] + '#' + s[:] + '#'