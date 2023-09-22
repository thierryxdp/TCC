def retira_pontuacao(s):
    ''' Função que retira a pontuacao de uma str;str->str'''
    s=str.replace(s,':',)
    s=str.replace(s,';',)
    s=str.replace(s,'.',)
    s=str.replace(s,'?',)
    s=str.replace(s,',',)
    s=str.replace(s,'-',)
    s=str.replace(s,'!',)
    s=str.replace(s,'  ',)
    s=s.strip()
    return s