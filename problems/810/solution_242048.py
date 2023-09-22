def retira_pontuacao (frase):
    '''recebe uma frase, calcula  e retorna uma frase onde os caracteres de pontuação são substituídos por espaço'''
    '''str->str'''
    um =  str.replace (frase,'-',' ')
    dois =  str.replace (um,',',' ')
    tres = str.replace (dois ,':',' ')
    quatro = str.replace (tres,';',' ')
    quinto = str.replace (quatro, '.',' ')
    sexto = str.replace (quinto, '!',' ')
    setimo = str.replace (sexto, '?',' ')
    return setimo

def minusculas (retira_pontuacao):
    str.lower (retira_pontuacao(frase))