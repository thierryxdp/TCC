def posLetra (string, letra, n):
    """Função que retorna a letra pedida input str, str, int, return int or str"""
    contador = qtd_achados = 0
    while contador < len(string):
        if n <= string.count(letra):
            if string[contador] == letra and qtd_achados < n:
                return qtd_achados += 1
        else:
            return -1
        contador += 1
    return qtd_achados