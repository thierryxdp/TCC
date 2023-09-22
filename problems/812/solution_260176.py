def retira_pontuacao(txt):
    x = txt.split('-')
    c = x
    c = txt.split(',')
    b = c
    b = txt.split(':')
    z = b
    z = txt.split(';')
    a = z
    a = txt.split('.')
    l=a
    l= txt.split('!')
    
    return str(l[0]+ l[1])