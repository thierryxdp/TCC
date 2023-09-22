def retira_pontuacao(frase):

    frase1 = str.replace(frase, ',', '')
    frase2 = str.replace(frase1,'.','')
    frase3 = str.replace(frase2,':','')
    frase4 = str.replace(frase3,';','')
    frase5 = str.replace(frase4,'!','')
    frase6 = str.replace(frase5,'-',' ')
    fraseFinal = str.replace(frase6,'?','')

    return fraseFinal

def inverte(frase):
    '''funcao que recebe uma frase, inverte a frase, retira pontuação e maiusculas
    str -> str'''
    frase1 = retira_pontuacao(frase)
    frase2 = str.lower(frase1)
    frase3 = str.split(frase2,' ')
    frase4 = list.reverse(frase3)
    
    
    return frase4