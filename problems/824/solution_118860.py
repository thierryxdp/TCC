def uppCons(frase):
    '''funcao que recebe uma frase de entrada e retorna essa mesma frase cim todas as suas consoantes em letras maiusculas;
    str->str'''
    f = ' '
    prox_letra = 0
    while frase[prox_letra] < len(frase):
        if frase[prox_letra] != 'a' and 'A' and 'e' and 'E' and 'i' and 'I' and 'o' and 'O' and 'u' and 'U':
            f = str.upper(frase[prox_letra])
        prox_letra = prox_letra + 1
    return f