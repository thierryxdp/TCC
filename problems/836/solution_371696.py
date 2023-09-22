def busca(setor, func):
    "Retorne os dados dos funcionários de um dado setor; str,lista(lista)->lista"
    l=[]
    if not setor in func[0]:
        return l