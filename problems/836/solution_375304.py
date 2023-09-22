def busca(informacao,registro):
    """Função que dada uma informação referente a nome, registro, setor ou telefone,
retorna os dados do funcionário; str,list->list"""
    resultado=[]
    for elemento in registro:        
        for dados in elemento:
            if str.lower(informacao)in str.lower(dados):
                del elemento[2]
                resultado.append(elemento)
    return resultado