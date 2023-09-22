def posLetra(string,letra,numero):
    """Função na qual dado uma string, uma letra e
    um numero que indica a ocorrencia desejada da letra,
    retorna em que posição da string a letra se encontra"""
    index = 0
    contador = 0
    soma = 0
    while contador <= numero:
        soma = soma + index
        index = str.find(string,letra,soma)
        contador += 1
    elif index != -1:
        return index
    else:
        return "Ocorrência não encontrada"