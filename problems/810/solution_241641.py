def retira_pontuacao (frase:str)-> str:
    '''dada uma frase, retorna a frase, porém com pontuação substituída por
    espaço'''
    frase= str.replace (frase, '-', ' ')
    frase= str.replace (frase, ',', ' ')
    frase= str.replace (frase, ':', ' ')
    frase= str.replace (frase, ';', ' ')
    frase= str.replace (frase, '...', ' ')
    frase= str.replace (frase, '.', ' ')
    frase= str.replace (frase, '?', ' ')
    frase= str.replace (frase, '!', ' ')
    return frase

def inverte (frase: str)-> str:
    '''retorna uma frase que contenha as palavras da frase dada na ordem
    inversa, sem letras maúsculas e sem pontuação'''
    frase = str.lower(frase)
    frase = str.split(frase)
    
    return frase[-1]+ ' ' + frase[-2] + ' ' + frase[-3]+ ' ' + frase[-4] + ' ' + frase[-5]+ ' ' + frase[-6] + ' ' + frase[-7]