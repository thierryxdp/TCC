def lingua_p(palavra):
    '''
    Funcao que recebe uma string. A funcao retorna uma nova string em minuscula aonde as vogais sao adicionadas a letra p + a vogal existente
    str -> str
    '''  
    nova_palavra = ''
    for letra in palavra:
        nova_letra = letra.lower()
        if nova_letra in 'aeiou':
            nova_letra = nova_letra + 'p' + nova_letra
        nova_palavra = nova_palavra + nova_letra

    return nova_palavra