def retira_pontuacao(s):
    '''retira todos os caracteres de pontuação e substitui por espaços
       str -> str'''
    s=str.replace(s,':',' ')
    s=str.replace(s,';',' ')
    s=str.replace(s,'.',' ')
    s=str.replace(s,',',' ')
    s=str.replace(s,'!',' ')
    s=str.replace(s,'?',' ')
    s=str.replace(s,'/',' ')
    s=str.replace(s,'-',' ')
    
    return s