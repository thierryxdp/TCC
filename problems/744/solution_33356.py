def hashtag(s):
    """dada uma string s de entrada retorna a mesma no entanto com um '#' no início, outro no
    meio e mais um no fim.
    str --> str"""
    s1=s[0:len(s)//2]
    s2=s[len(s)//2:len(s)]
    s3='#'+s1+'#'+s2+'#'
    return s3