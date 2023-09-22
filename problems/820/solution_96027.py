def posLetra (string: str, letra: str, ocorrencia: int) -> int:
    """Recebe uma string, uma letra e um número indicando possíveis ocorrências
    de letra em string, retorna qual é a posição da letra em sua ocorrencia-ésima
    caso o número de vezes que letra aparece em string seja menor que ocorrencia
    a função retorna -1."""
    contador_de_letra = 0
    tamanho_string = len(string)
    contador = 0
    while contador < tamanho_string and contador_de_letra < ocorrencia:
        if str.lower(string[contador]) == str.lower(letra):
        	contador_de_letra + = 1
        contador += 1
   	if contador_de_letra == ocorrencia
    	return contador
    else:
        return -1