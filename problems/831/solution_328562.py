#Questão 6
def lingua_p(palavraPt):
    """Função que traduz um palavra em português para a língua do P;
    str -> str"""
    listaPalavras = list(palavraPt)
    for p in range(len(listaPalavras)):
        if listaPalavras[p] in 'aeiouAEIOU':
            listaPalavras[p] = listaPalavras[p] + 'p' + listaPalavras[p]
    return ''.join(listaPalavras)