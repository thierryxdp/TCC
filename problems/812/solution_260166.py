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
    
    return str(a[0])