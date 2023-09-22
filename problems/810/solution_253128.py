def retira_pontuacao(frase):
    '''Função retira as pontuações da frase substituindo pelo caracter 'espaço' 
       str --> str'''
    l = frase.replace('.', ' ')
    l2 = l.replace(',',' ')
    l3 = l2.replace('-', ' ')
    l4 = l3.replace(':', ' ')
    l5 = l4.replace(';', ' ')
    l6 = l5.replace('?', ' ')
    l7 = l6.replace('!', ' ')
    return l7

def inverte(frase):
    l = retira_pontuacao(frase)
    l1 = l.lower()
    l2 = l1.split()
    l3 = l2[::-1]
    l4 = ' '.join(l3)
    return l4