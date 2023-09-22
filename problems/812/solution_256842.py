def retira_pontuacao(frase):
    '''Função que retira a pontuação de uma frase e substitui por espaço.'''
    for caractere in '!':
        frase = frase.replace(caractere, ' ')
    for caractere in '?':
        frase = frase.replace(caractere, ' ')
    for caractere in '.':
        frase = frase.replace(caractere, ' ')
    for caractere in ':':
        frase = frase.replace(caractere, ' ')
    for caractere in '...':
        frase = frase.replace(caractere, ' ')
    for caractere in '-':
        frase = frase.replace(caractere, ' ')
    for caractere in ';':
        frase = frase.replace(caractere, ' ')
        return frase