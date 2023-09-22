def posLetra (frase: str,letra: str,numero: int) -> int:
    """Função que recebe uma frase, uma letra e um número referente à ocorrência desejada da letra
    e retorna a posição da string que aquela ocorrência está. Caso exista menos ocorrências do
    que a ocorrência desejada, o retorno será -1."""
    inicio = 0
    fim = len(frase)
    while numero != str.index(frase, letra, inicio, fim):
        inicio = str.index(frase,letra,inicio,fim) + 1
    return inicio