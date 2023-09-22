def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a mesma frase substituindo os caracteres de pontuação por espaço.  ent-> string  saida-> string'''
    
    
    lista = frase.split(',', '.')
    
    lista2 = ' '.join(lista)
    
    return lista2