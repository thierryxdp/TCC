def retira_pontuacao(frase):
    '''
    Função que retorna a frase com todos os caracteres de 
    pontuação da frase dada substituídos por espaços
    '''
    frase1=frase.replace('-',' ')
    frase2=frase1.replace(',',' ')
    frase3=frase2.replace(':',' ')
    frase4=frase3.replace(';',' ')
    frase5=frase4.replace('.',' ')
    frase6=frase5.replace('!',' ')
    frase7=frase6.replace('?',' ')
    
    return frase7

def inverte(frase):
    '''
    Função que dada uma frase, retorna outra frase que contem
    as mesmas palavras da frase de entrada, porém na ordem inversa,
    sem letras maiúsculas e sem pontuação
    '''
    frase1=retira_pontuacao(frase)
    frase2=frase1.lower()
    frase3=reversed(frase2)
    
    
    
    return frase3