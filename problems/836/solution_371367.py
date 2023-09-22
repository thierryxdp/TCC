def busca(buscandoPor,matriz):
    resultado=[]
    for nome,registro,setor,fone in matriz:
        if setor==buscandoPor:
            resultado.append([nome,registro,fone])
    return resultado
'''funcao que recebe um setor de busca e uma matriz com os 
dados de uma empresa, e retorna os dados dos funcionarios do setor
dado como parametro
str,list->list'''