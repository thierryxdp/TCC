def busca(informacao,registro):
    """Função que dada uma informação referente a nome, registro, setor ou telefone,
retorna os dados de todos os funcionários daquele setor; str,list->list"""
    lista=[]
    for elemento in registro:
        for dados in elemento:
            if str.lower(informacao)==str.lower(dados):
                lista.append(elemento)
    return lista