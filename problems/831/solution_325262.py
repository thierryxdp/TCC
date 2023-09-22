def lingua_p(palavra):
    '''lingua_p recebe uma palvra em português e devolve a mesma palavra traduzida para a lingua P.
    Ao traduzir para a lingua P, toda vogal passa a ser antecedida e seguida por p.
    str-->str'''
    index=1
    palavra1=[]
    for vogal in str.lower(palavra):
        palavra1.append(vogal)
        if vogal in ['a','e','i','o','u','ã','é','á','í','ó','ú','õ','à']:
            palavra1.insert(index, "p"+vogal)
            index=index+2
        index=index+1
    return str.join("",palavra1)