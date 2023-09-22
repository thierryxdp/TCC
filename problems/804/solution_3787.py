def filtra_pares(tupla):
    """ A Função chamada filtra pares, vai receber uma tupla contendo quatro números inteiros e retorna uma
    nova tupla com apenas os números pares, na mesma ordem em que eles se encontravam. """
    tupla_vazia=()
    if tupla[0]%2==0:
       tupla_vazia=tupla_vazia + (tupla[0],)
    if tupla[1]%2==0:
       tupla_vazia=tupla_vazia + (tupla[1],)
    if tupla[2]%2==0:
       tupla_vazia=tupla_vazia + (tupla[2],)
    if tupla[3]%2==0:
       return tupla_vazia + (tupla[3],)
    else:
       return tupla_vazia