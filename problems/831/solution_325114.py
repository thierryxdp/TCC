def lingua_p(palavra):
    '''recebe uma palavra em português e traduz para a língua do P, ou seja, apos cada vogal da palavra adiciona a combinação p+vogal
    str -> str'''
    palavra = str.lower(palavra)
    vogais = ['a','e','i','o','u','á','é','í','ó','ú','ã','õ','â','ê','î','ô','û','à']
    qntvogais = 0
    for i in vogais:
        qntvogais = qntvogais + palavra.count(i)
    tamanho = len(palavra)+2*qntvogais
    for n in range(tamanho):
        if palavra[n] in vogais:
            v = palavra[n]
            palavra = palavra.replace(v, str.upper(v+'p'+v)) 
    return str.lower(palavra)