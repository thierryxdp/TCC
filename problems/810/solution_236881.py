def inverte(string):
    """Dada uma frase remove a pontuação, as letras maiúsculas e
    a retorna essa mesma frase com a ordem dos caracteres invertida."""
    remove = string.replace('-',' ')
    remove = remove.replace(',',' ')
    remove = remove.replace(':',' ')
    remove = remove.replace(';',' ')
    remove = remove.replace('!',' ')
    remove = remove.replace('?',' ')
    remove = remove.replace('...',' ')
    remove = remove.replace('.',' ')
    minuscula = remove.lower()
    separa = minuscula.split()
    separa_invertida = separa[::-1]
    return str.join(' ',(separa_invertida))