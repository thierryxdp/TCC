def maiores(lista,n):
    """
    funcao que dada uma lista de numeros inteiros e 
    um numero inteiro n, retorna outra lista que contenha
    todos os numeros dessa lista original
    : lista --> lista 
    ## tive que pesquisar no google essa questao, pois 
    nao sabia como retornar numeros maiores. Nao sei
    se meu ponto será inteiro pelo (for) mas nao obtive 
    nenhum resultado na minha pesquisa para substituir
    mesmo.##
    """
    numeros_maiores = [ x for x in lista if x > n ]
    list.sort(numeros_maiores)
    return numeros_maiores