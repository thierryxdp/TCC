def busca(setor, func):
    "Retorne os dados dos funcionários de um dado setor; str,lista(lista)->lista"
    l=[]
    for i in func:
        
        for j in i:
            ll=[]
            if j==setor:
                ll.append(i)
        l.append(ll)
    return l