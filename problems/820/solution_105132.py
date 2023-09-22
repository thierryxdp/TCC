def posLetra(string,letra,num):
    """função deve retornar em que posição da sting aquelao ocorrência da letra está.Caso exista menos ocorrências da letra do que a ocorrência perdida, a função deve retornar -1."""
    if string.count(letra)>=num:
        return string.find(letra,num-1)
    else:
        return -1