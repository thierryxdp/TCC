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
    '''Dada uma frase, retorna outra frase que contenha as mesmas palavras
    da frase de entrada na ordem inversa, sem letras maiúsculas e sem a 
    pontuação.'''
    txt = retira_pontuacao(texto)
    txt = txt.split()
    txt.reverse()
    txt = str.join(' ',txt)

    return txt.lower()