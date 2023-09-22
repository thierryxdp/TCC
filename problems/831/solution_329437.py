def lingua_p(palavra):
    ''' recebe uma palavra e traduz ela para lingua p, ou seja, depois de cada vogal adiciona um p mais a própria vogal
    str->str'''
    nova_palavra=''
    for i in palavra:
        if i in 'aeiouAEIOU' :
                nova_palavra= nova_palavra + i + 'p' + i
        else:
            nova_palavra= nova_palavra + i
    return nova_palavra