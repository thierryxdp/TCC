def uppCons(frase):
    ''' funcao que recebe uma frase e retorna a mesma frase so que com as consoantes em letra maiuscula. str -> str.'''
    frase_nova = frase.upper()
    if 'A' in frase_nova:
        frase_nova.replace('a','A')
    if 'E' in frase_nova:
        frase_nova.replace('E','e')
    if 'I' in frase_nova:
        frase_nova.replace('I','i')
    if 'O' in frase_nova:
        frase_nova.replace('O','o')
    if 'U' in frase_nova:
        frase_nova.replace('U','u')
    return frase_nova