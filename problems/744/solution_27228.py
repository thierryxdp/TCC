def hashtag (s):
    """ recebe uma string 's' e insere o caractere "#" no início, no meio
    e no final dela.
    str -> str """
    b = len(s)//2
    return "#"+s[:b]+"#"+s[b:]+"#"