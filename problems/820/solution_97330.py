def posLetra (frase: str, letra: str, numero: int) -> int:
    """Função que recebe uma frase, uma letra e um número que indica a ocorrência desejada, 
    e retorna em que poisção da string aquela ocorrência da letra está. Caso exista menos ocorrências
    da letra do que a ocorrência pedida, retorna -1."""
    fim = len(frase)
    inicio = 0
    while str.index(frase, letra, inicio, fim) != numero:
        soma = str.index(frase,letra,inicio,fim)
        inicio = inicio + soma
  	return inicio
 	if str.index(frase,letra,inicio,fim) < numero:
           	 return -1