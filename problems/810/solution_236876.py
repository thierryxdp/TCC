def invertida(string):
    """Dada uma frase remove a pontuação, as letras maiúsculas e
    a retorna essa mesma frase com a ordem dos caracteres invertida."""
    sem_ponto = retira_pontuacao(string)
    minuscula = sem_ponto.lower()
    separa = minuscula.split()
    separa_invertida = separa[::-1]
    return str.join(' ',(separa_invertida))