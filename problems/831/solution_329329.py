def lingua_p(palavra):
    ''' recebe uma palavra e traduz ela para lingua p, ou seja, depois de cada vogal adiciona um p mais a própria vogal
    str->str'''
    for i in palavra:
        if i == 'aeiouAEIOU':
           	posicao= palavra.index(i)
            palavra= str(palavra[0:posicao+1]) + 'p' + i + str(palavra[i+1:])
    return palavra