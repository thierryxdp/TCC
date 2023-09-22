def retira_ponctuacao(frase):
    '''funcao que dada uma frase retorna a frase onde todos os caracteres de ponctuacao tenham sido substituidos por espaco
    str->str'''
    f1=str.replace(frase,',','')
    f2=str.replace(f1,'-','')
    f3=str.replace(f2,':','')
    f4=str.replace(f3,';','')
    return f4