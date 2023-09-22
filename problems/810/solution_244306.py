def retira_pontuacao(frase):
    '''
    	Funcao recebe uma string com uma frase 
        e retorna a frase com todos os caracteres 
        de pontuacaoo substituidos por espaço
        str -> str
    '''
    return ((((((((frase.replace('-',' ')).replace(',',' ')).replace(';',' ')).replace(':',' ')).replace('.',' ')).replace('!',' ')).replace('?',' ')).replace('...',' '))

def inverte(frase):
    '''
    	Funcao recebe uma frase e retorna
        uma outra frase que contenha as mesmas
        palavras da frase dada na ordem inversa,
        sem letras maiúsculas e sem pontuacao
        str -> str
        
    '''
    frase = retira_pontuacao(frase)
    frase = frase.split(' ')
    list.reverse(frase)
    frase = ' '.join(frase)
    frase = str.lower(frase)

    return frase