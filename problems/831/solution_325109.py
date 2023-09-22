def lingua_p(palavra):
    palavra = str.lower(palavra)
    vogais = ['a','e','i','o','u']
    qntvogais = 0
    for i in vogais:
        qntvogais = qntvogais + palavra.count(i)
    tamanho = len(palavra)+2*qntvogais
    for n in range(tamanho):
        if palavra[n] in 'aeiou':
            v = palavra[n]
            palavra = palavra.replace(v, str.upper(v+'p'+v)) 
    return str.lower(palavra)