#Questão 4
def retira_pontuacao(frase):
    '''Função que retira a pontuação de uma frase e substitui por espaço.'''
    for caractere in '!':
        frase = frase.replace(caractere, '')
    for caractere in '?':
        frase = frase.replace(caractere, '')
    for caractere in '.':
        frase = frase.replace(caractere, '')
    for caractere in ':':
        frase = frase.replace(caractere, '')
    for caractere in '...':
        frase = frase.replace(caractere, '')
    for caractere in '-':
        frase = frase.replace(caractere, ' ')
    for caractere in ';':
        frase = frase.replace(caractere, '')
    for caractere in ',':
        frase = frase.replace(caractere, ' ')
        return frase

#Questão 5
def inverte(frase):
    '''Função que retorna a mesma frase de entrada só que na ordem inversa,
    e sem pontuação.'''
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = str.split(frase,' ')
    frase = str.join(' ',frase[::-1])
    return frase