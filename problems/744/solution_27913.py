def hashtag(s):
    '''Retorna uma string com o caractere "#" insirido no início, no meio e no final dela;
    str -> str'''
    meio = len(s)//2
    return "#"+s[:meio]+"#"+s[meio:]+"#"