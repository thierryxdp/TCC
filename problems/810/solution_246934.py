def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a mesma frase substituindo os caracteres de pontuação por espaço.  ent-> string  saida-> string'''
    
    
    lista1 = frase.split(',')
    lista2 = ''.join(lista1)
    lista3 = lista2.split('.')
    lista4 = ''.join(lista3)
    lista5 = lista4.split('-')
    lista6 = ' '.join(lista5)
    lista7 = lista6.split('?')
    lista8 = ''.join(lista7)
    lista9 = lista8.split('!')
    lista10 = ''.join(lista9)
    
    return lista10

def inverte(frase):
    ''' Função que dada uma frase, retorna uma outra frase que contenha as mesmas palavras em ordem inversa a frase de entrada, sem pontuação e sem letras maiusculas.  ent-> str   saida-> str  '''
    
    frase = retira_pontuacao(frase)    
    lista = frase.split(' ')
    newlista = []
    newlista = lista[::-1]
    newoldlista = ' '.join(newlista)
    
        
    return str.lower(newoldlista)