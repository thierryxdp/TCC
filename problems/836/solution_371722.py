def busca(setor, func):
    "Retorne os dados dos funcionários de um dado setor; str,lista(lista)->lista"
    l=[]
    for i in func:
        for j in i:
            if j==setor:
                l.extend((i[:2],i[-1]))
        
    return l