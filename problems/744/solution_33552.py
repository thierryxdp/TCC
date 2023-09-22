def hashtag(s):
    '''Função que receba uma string e insera o caractere # no início, no meio e no final dela; string -> string'''
    if len(s%2)==0:
        return str(s[:2])+'#'+str(s[2:])