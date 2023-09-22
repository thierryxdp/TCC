def retira_pontuacao(s):
    '''retira todos os caracteres de pontuação e substitui por espaços
       str -> str'''
    str.replace(s,':',' ')
    str.replace(s,';',' ')
    str.replace(s,'.',' ')
    str.replace(s,',',' ')
    str.replace(s,'!',' ')
    str.replace(s,'?',' ')
    str.replace(s,'/',' ')
    str.replace(s,'-',' ')
    
    return s