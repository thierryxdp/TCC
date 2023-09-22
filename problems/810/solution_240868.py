def retira_pontuacao(frase):
    '''Dada uma frase, retorna todos os caracteres de pontuação substituídos por espaços; string -> string'''
    return frase.replace('...',' ').replace('.',' ').replace('?',' ').replace('!',' ').replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ')

def inverte(frase):
    '''Dada uma frese, retorna outra frase que contem as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas e sem a pontuação; string -> string'''
    frase_lista = str.lower(retira_pontuacao(frase)).split(' ')
    frase_lista_inversa = frase_lista[-1::-1]
    return str.join(' ',frase_lista_inversa).strip()