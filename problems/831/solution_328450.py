#Questão 6
def lingua_p(plavaraPt):
    """Função que traduz um palavra em português para a língua do P;
    str -> str"""
    listaPalavras = list(palavraPt)
    for p in listaPalavras:
        if p in 'aeiou':
            str.replace(listaPalavras, p, p+'p')
    return list.join(listaPalavras)