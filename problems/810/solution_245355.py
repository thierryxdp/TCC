def retira_pontuacao(frase):
    '''dada uma frase, retorna a mesma sem pontuação
str-->str'''
    frase1=str.replace(frase,'-',' ')
    frase2=str.replace(frase1,',',' ')
    frase3=str.replace(frase2,':',' ')
    frase4=str.replace(frase3,';',' ')
    frase5=str.replace(frase4,'.',' ')
    frase6=str.replace(frase5,'!',' ')
    frase_final=str.replace(frase6,'?',' ')
    return frase_final

def inverte(frase):
    """apos retirar a pontuaçao e transformar as letras maiusculas em minusculas, retorna o inverso da frase dada"""
    """str -> str"""
    
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    l = str.split(frase)
    list.reverse(l)
    
    return str.join(" ",l)