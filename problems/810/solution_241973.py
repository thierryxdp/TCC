def retira_pontuacao(frase):
    '''
    dada uma frase, retorna ela mesma mas com sua
    pontuação substituída por espaços
    
    string -> string
    '''
    
    frase = frase.replace(',', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace('.', '')
    frase = frase.replace(',', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('!', '')
    frase = frase.replace('?', '')
    frase = frase.replace(':', ' ')
    return frase

def inverte(frase2):
    '''
    dada uma frase, retorna a mesma frase
    mas sem pontuação, em ordem invertida e
    com todas as letras minúsculas
    
    string -> string
    '''
    
    texto = frase2.lower()
    texto = retira_pontuacao(texto)
    texto = texto.split()
    texto.reverse()
    texto = ' '.join(texto)
    return texto