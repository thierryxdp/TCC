def consoantesmaiusculas(frase):
    '''Função que recebe uma frase e a edita para que todas as
consoantes sejam maiúsculas sem mexer no resto dos caracteres.
Entrada:
    frase: str
Saída:
    str'''
    vogais = ('a', 'e', 'i', 'o', 'u')
    editada = ''
    i = 0
    while i < len(frase):
        if frase[i].isalpha() and frase[i] not in vogais:
            editada += frase[i].upper()
        else:
            editada += frase[i]
        i += 1
    return editada