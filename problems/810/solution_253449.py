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
    mm = texto.lower()
    sep = texto.split(' ')
    
    return mm(retira_pontuacao(texto)[sep::-1])