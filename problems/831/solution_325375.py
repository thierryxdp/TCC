def lingua_p(palavra):
    '''Função que recebe palavra em português e a traduz para a língua do p; str->str'''
    palavranova=''
    for i in palavra:
        if i in 'aeiouAEIOU':
            palavranova = palavranova + i + 'p' + i
        else:
            palavranova = palavranova + i
    return str.lower(palavranova)