def posLetra(texto:str,letra:str,num:int)-> str:
    """Recebe um texto, uma letra e sua ocorrência e retorna seu exato índice."""
    if texto.count(letra) < ocorrencia:
        return -1
    else:
        i = 0
        letras = []
        caracteres = list(texto)
        while i < len(caracteres) and len(letras) < ocorrencia:
            if letra == caracteres[i]:
                list.append(letras, caracteres[i])
            i = i + 1
        return i - 1