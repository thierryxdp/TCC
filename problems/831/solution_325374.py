def lingua_p(palavra):
    '''Função que recebe palavra em português e a traduz para a língua do p; str->str'''
    for i in palavra:
        if i in 'aeiouAEIOU':
            str.replace(palavra,i,i+'p'+i)
    return str.lower(str.replace(palavra,i,i+'p'+i))