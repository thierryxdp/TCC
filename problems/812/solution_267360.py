def retira_pontuacao(frase):
    ''''''
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
   
    return frase