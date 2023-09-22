def hashtag(s):
    """recebe uma string e insere um # no início, meio e fim
    str -> str"""
    pos_meio= len(s)//2
    return "#"+s[0:pos_meio]+"#"+s[pos_meio:]+"#"