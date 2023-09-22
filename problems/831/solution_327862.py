def lingua_p(palavra):
    '''Função que recebe uma palavra e retorna
    a mesma traduzida para a lingua do P;
    entrada: str
    saída: str'''
    lingua = ''
    for letra in range(len(palavra)):
        if palavra[letra] in ('a','A','e','E','i','I','o','O','u','U'):
            lingua += palavra[letra] + 'p' + palavra[letra]
        else:
            lingua += palavra[letra]
    return lingua.lower()