def inverte(s):
      char_replace = ['!','?','.',',',';','-',':','...']
    for char in char_replace:
        s = s.replace(char,' ')
    x=str.split(s)
    return x[::-1]