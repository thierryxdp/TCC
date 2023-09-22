def retira_pontuacao(s):
    char_replace = ['!','?','.',',',';','-',':','...']
    for char in char_replace:
        s = s.replace(char,' ')
    return s