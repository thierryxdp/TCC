def inverte(frase):
    '''Função que, dada uma frase qualquer, retorna a mesma
    frase com as palavras na ordem inversa sem letras 
    maiúculas e pontuação'''
    def retira_pontuacao(frase):
        
    frase1=frase.replace('-', ' ')
    frase2=frase1.replace(',', ' ')
    frase3=frase2.replace(':', ' ')
    frase4=frase3.replace(';', ' ')
    frase5=frase4.replace('.', ' ')
    frase6=frase5.replace('!', ' ')
    frase7=frase6.replace('?', ' ')
    return frase7
    
    frase_sem_pont_min = retira_pontuacao(frase).lower()
    lista = frase_sem_pont_min.split()
    lista_invertida = lista.reverse()
    return (' '.join(lista))