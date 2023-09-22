def busca(setor, func):
    "Retorne os dados dos funcionários de um dado setor; str,lista(lista)->lista"
    
    for i in func:
        ll=[]
        for j in i:
            if j==setor:
                ll.append(i)
    return ll