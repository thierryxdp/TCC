def hashtag(s):
    """ Dado uma sring, retorna elas com uma hastag no início, meio e no final dela; str -> str"""
    a = len(s)
    b = a//2
    return str('#') + str(s[:b])+ str('#')+ str(s[b:]) + str('#')