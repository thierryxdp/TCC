def hashtag(s):
    '''Função que recebe uma string e insere o caractere
    "#" no início, no meio e no final dela'''
    return "#"+s[:len(s)//2]+"#"+s[len(s)//2:]+"#"