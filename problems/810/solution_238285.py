def inverte(frase):
    """Função que inverte a ordem das palavras de uma frase;
    str -> str"""
    sem_pontuacao = str.replace(str.replace(str.replace( str.replace( str.replace( str.replace(str.replace(str.replace(frase, ',', ' '), '.', ' '), '/', ' '), ':', ' '), ';', ' '), '!',' '),'?', ' '),'-',' ')
    lista_palavras = str.split(sem_pontuacao)
    ordem_inversa = lista_palavras[ : : -1]
    frase_invertida = str.join(' ', ordem_inversa)
    return str.strip(str.lower(frase_invertida))