def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a mesma frase substituindo os caracteres de pontuação por espaço.  ent-> string  saida-> string'''
    
    
    lista1 = frase.split(',')
    lista2 = ' '.join(lista1)
    lista3 = lista2.split('.')
    lista4 = ' '.join(lista3)
    lista5 = lista4.split('-')
    lista6 = ' '.join(lista5)
    
    return lista6