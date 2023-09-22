def inverte(frase):
    '''recebe uma frase e a retorna sem pontuação, toda minúscula e inversa
    	str->str'''
    
    frase2=frase.replace('...',' ',-1)
    frase3=frase2.replace('.',' ',-1)
    frase4=frase3.replace(',',' ',-1)
    frase5=frase4.replace(';',' ',-1)
    frase6=frase5.replace('?',' ',-1)
    frase7=frase6.replace('-',' ',-1)
    frase8=frase7.replace('!',' ',-1)
    frase9=frase8.replace(':',' ',-1)
    
    nova_frase=frase9.lower()
    palavras=nova_frase.split(' ')
    frase_invertida=' '.join(reversed(palavras))
    
    return frase_invertida