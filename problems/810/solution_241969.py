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
    texto = texto.split()
    texto = str(reverse(texto))
    texto = retira_pontuacao(texto)
    return texto