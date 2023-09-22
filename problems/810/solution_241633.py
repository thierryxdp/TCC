def inverte(frase):
    '''Função que, dada uma frase qualquer, retorna a mesma 
    frase com as palavras na ordem inversa sem letras
    maiúsculas, e sem pontuação'''
    frase_sem_pont_min = retira_pontuacao(frase).lower()
    lista = frase_sem_pont_min.split()
    lista_invertida = lista.reverse()
    return (' '.join(lista))