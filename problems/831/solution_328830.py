def lingua_p(palavra):
    '''Recebe uma palavra e retorna a mesma palavra
    com a letra "p" e a vogal original despois de toda vogal; str -> str'''
    palavra_em_p = ''
    for i in palavra:
        if i in 'AEIOUaeiouÁÉÍÓÚáéíóúâêôÂÊÔ':
            palavra_em_p += 'p' + i
        else:
            palavra_em_p += i
    return palavra_em_p