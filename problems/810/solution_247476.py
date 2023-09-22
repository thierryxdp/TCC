def inverte(frase):
    """A função recebe como entrada uma frase (string) e a retorna (string)
    invertida (a primeira palavra se torna a última, assim por diante), mas
    com todas as letras minúsculas e sem caracteres de pontuação."""
    frase_minuscula = frase.lower()
    frase_sem_pontuacao = substitui_por_espaco(frase_minuscula)
    lista = frase_sem_pontuacao.split()
    lista_invertida = lista[::-1]
    return ' '.join(lista_invertida)