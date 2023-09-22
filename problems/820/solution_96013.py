def posLetra(texto,letra,ocorrencia_letra):
    """Esta função recebe um texto, uma letra e a ocorrência desta letra no texto e retorna a posição desta ocorrência no texto, se não tiver a função retorna -1
    str,str,int -> int"""
    i = 1
    j = 0
    new_texto = texto
    if texto.count(letra) >= ocorrencia_letra:
        while i < ocorrencia_letra:
            novo_texto = new_texto[:ocorrencia_letra-j]+new_texto[ocorrencia_letra-j:]
            i += 1
            j += 1
        return (novo_texto.find(letra) + i-1)
    else:
        return -1