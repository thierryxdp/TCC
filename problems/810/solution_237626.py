def inverte(s):
    char_replace = ['!','?','.',',',';','-',':','...']
    for char in char_replace:
        s = s.replace(char,' ')
    s=str.split(s)
    r= s[::-1]
    return str(r)