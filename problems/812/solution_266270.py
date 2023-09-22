def retira_pontuacao(frase):
    '''retorna a frase com as pontuações substituídas por espaço;
    str->str'''
    
    f1=str.replace(frase,',',' ')
    f2=str.replace(f1,'-',' ')
    f3=str.replace(f2,':',' ')
    f4=str.replace(f3,'...',' ')
    f5=str.replace(f4,'.',' ')
    f6=str.replace(f5,'!',' ')
    f7=str.replace(f6,'?',' ')
    f8=str.replace(f7,';',' ')
    
    return f8