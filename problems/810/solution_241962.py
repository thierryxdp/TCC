def retira_pontuacao(frase):
    '''
    dada uma frase, retorna ela mesma mas com sua
    pontuação substituída por espaços
    
    string -> string
    '''
    
    frase = frase.replace(',', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace(':', ' ')
    return

def inverte(frase2):
    '''
    dada uma frase, retorna a mesma frase
    mas sem pontuação, em ordem invertida e
    com todas as letras minúsculas
    
    string -> string
    '''
    texto = retira_pontuacao(frase2)
    texto = texto.lower()
    texto = texto[::-1]
    return texto