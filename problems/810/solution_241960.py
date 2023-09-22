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

def inverte(frase):
    '''
    dada uma frase, retorna a mesma frase
    mas sem pontuação, em ordem invertida e
    com todas as letras minúsculas
    
    string -> string
    '''
    x = retira_pontuacao(frase)
    x = x.lower()
    x = texto[::-1]
    return x