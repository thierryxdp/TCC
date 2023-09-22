def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário(dic), que cada palavra dessa string seja uma chave(c) e tenha como valor o número de vezes(x) que a palavra aparece"""
    """str->dict"""
    dic={'c':'x'}
    dim=str.split(frases,' ')
    for y in range(len(dim)):
        dic[dim[y]]=list.count(dim,dim[y])
    del(dic)['c']
    return dic