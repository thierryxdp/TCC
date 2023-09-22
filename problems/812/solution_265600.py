def retira_pontuacao(frase):
    '''Dado uma frase, a função deve retornar a frase onde 
    todas as pontuações sejam substituídos por espaços;
    str -> str'''
    frase1=(str.replace(frase,'!',' '))
    
    frase2=(str.replace(frase1,'?',' '))
    
    frase3=(str.replace(frase2,'...',' '))
    
    frase4=(str.replace(frase3,'.',' '))
    
    frase5=(str.replace(frase4,',',' '))
    
    frase6=(str.replace(frase5,';',' '))
    
    frase7=(str.replace(frase6,':',' '))
    
    frase8=(str.replace(frase7,'-',' '))
    
    return frase8