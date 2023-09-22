def lingua_p(palavra):
    ''' recebe uma palavra e traduz ela para lingua p, ou seja, depois de cada vogal adiciona um p mais a própria vogal
    str->str'''
    nova_palavra=()
    for i in palavra:
        if i in 'aeiouAEIOU' :
                posicao= palavra.index(i)
                nova_palavra= str(palavra[0:posicao+1]) + 'p' + i 
    return nova_palavra