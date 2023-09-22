#Questão 6
def lingua_p(palavraPt):
    """Função que traduz um palavra em português para a língua do P;
    str -> str"""
    listaPalavras = list(palavraPt)
    for p in listaPalavras:
        if p in 'aeiouAEIOU':
            listaPalavras.insert(p, +'p')
    return list.join(listaPalavras)