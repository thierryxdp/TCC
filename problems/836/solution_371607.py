def busca (chave,matriz):
    '''dado um nome de um setor da empresa,
    a função retorna os dados de todos os funcionários daquele setor
    str, list -> list'''
    pessoa1 = matriz[0]
    pessoa2 = matriz[1]
    pessoa3 = matriz[2]  
    if chave in pessoa1 and pessoa3:
        list.remove(pessoa1,chave)
        list.remove(pessoa3,chave)
        dados = [pessoa1] + [pessoa3]
    elif chave in pessoa1:
        list.remove(pessoa1,chave)
        dados = [pessoa1]
    elif chave in pessoa2:
        list.remove(pessoa2,chave)
        dados = [pessoa2]
    elif chave in pessoa3:
        list.remove(pessoa3,chave)
        dados = [pessoa3]
    else: 
        dados = []
    return dados