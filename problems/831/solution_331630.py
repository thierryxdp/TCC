def lingua_p(portuga):
    '''funcao que recebe uma palavra em portugues e retorna uma
       palavra que apos cada vogal da palavra original e inserida 
       a letra 'p' seguida da vogal original.
       str -> str'''
    i= 0
    final= ''
    for i in range(len(portuga)):
        if portuga[i] in 'aeiouáéíóúãõ':
            final += portuga[i] + 'p' + portuga[i]
        else: 
            final += portuga[i]
        i += 1
    return final