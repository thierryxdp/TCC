def hashtag(s):
    '''recebe uma string e inseri o caractere ”#” no início, no meio e no final dela.
    Por exemplo, se a entrada for ”abcd”, a saída deve ser ”#ab#cd#”.
    Entrada->str
    saida-> str '''
    s = '#'+ s[0:(len(s)//2)] + '#' + s[(len(s)//2):]+ '#'
    return s