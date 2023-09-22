def posLetra (string,letra,n):
    """funcao que retorna onde esta a letra pedida input str, str, int. return int or str"""
    index = 0
    contador = 0
    soma = 0
    while contador <= n:
        soma = soma + index
        index = str.find(string,letra,soma)
        contador = contador + 1

    if index != -1:
        return index
    else:
        return "Ocorrência não encontrada"