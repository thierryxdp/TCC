def hashtag(s):
    '''Função que dado uma string s adicione um "#" no início, meio e final dela
    str -> str'''
    PosicaoDoMeio = len(s) // 2
    StrAntesDoMeio = s[:PosicaoDoMeio]
    StrDepoisDoMeio = s[PosicaoDoMeio:]
    return '#' + StrAntesDoMeio + '#' + StrDepoisDoMeio + '#'