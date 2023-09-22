def retira_pontuacao(frase):
    '''Dada uma frase como parâmetro, a função retira toda a pontuação
    e substitui por espaço vazio.'''
    f = frase.split('_')
    frase = ' '.join(f)
   
    f = frase.split(',')
    frase = ' '.join(f)
   
    f = frase.split(':')
    frase = ' '.join(f)
   
    f = frase.split(';')
    frase = ' '.join(f)
   
    f = frase.split('.')
    frase = ' '.join(f)
    
    f = frase.split('-')
    frase = ' '.join(f)
    
    f = frase.split('?')
    frase = ' '.join(f)
    
    f = frase.split('!')
    frase = ' '.join(f)
   
    return frase

def inverte(texto):
    txt = retira_pontuacao(texto)
    string = str.split(txt)
    txt.reverse()
   
    return lower.texto