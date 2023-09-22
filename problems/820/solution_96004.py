def posLetra(texto,letra,ocorrencia_letra):
    """Esta função recebe um texto, uma letra e a ocorrência desta letra no texto e retorna a posição desta ocorrência no texto, se não tiver a função retorna -1
    str,str,int -> int"""
    i = 1
    new_texto = texto
    if texto.count(letra) >= ocorrencia_letra:
        while i <= ocorrencia_letra:
            new_texto = new_texto.replace(letra,"")
            i += 1
        return (new_texto.find(letra) + i-1)
    else:
        return -1