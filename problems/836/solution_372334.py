def busca(setor_busca,matriz):
    '''uma fun ̧c ̃ao chamada busca que receba uma string e 
    uma matriz como a do exemplo e fa ̧ca uma busca por 
    setor, ou seja, dado o nome de um setor da empresa, 
    a fun ̧c ̃ao retorna uma lista com os dados de todos os
    funcion ́arios daquele setor. str,matriz->matriz'''
    dados = []
    for nome, registro, setor, fone in matriz:
        if setor == setor_busca:
             dados.append([nome, registro, fone])
    return dados