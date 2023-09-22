def retira_pontuacao(string):
    a = str.replace(string,'!', ' ')
    b = str.replace(a,'?', ' ')    
    c = str.replace(b,'...', '[')
    d = str.replace(c,'[', ' ')
    e = str.replace(d,'-', ' ')
    f = str.replace(e,',', ' ')
    g = str.replace(f,';', ' ')      
    h = str.replace(g,':', ' ')
    i = str.replace(h,'.', ' ')

    return i