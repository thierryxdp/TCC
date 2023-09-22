def retira_pontuacao(s):
    s1 = str.replace(s,',','.')
    s2 = str.replace(s1,'-','.')
    s3 = str.replace(s2,'?','.')
    s7 = str.replace(s3,'!','.')
    s4 = str.replace(s7,';','.')
    s5 = str.split(s4,'.')
    s6 = str.join(' ',s5)
    return s6