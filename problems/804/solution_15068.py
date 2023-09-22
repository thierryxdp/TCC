def filtra_pares(tupla):
    """essa função recebe uma tupla com quatro elementos inteiros como argumento, e retorna uma nova
tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam.
caso nenhum dos elementos da tupla de entrada seja par, a função retorna 
uma tupla vazia.
tuple - > tuple """
    tupla_retorno=()
    if tupla[0]%2==0:
        tupla_retorno= tupla_retorno + (tupla[0],)
    if tupla[1]%2==0:
        tupla_retorno= tupla_retorno + (tupla[1],)
    if tupla[2]%2==0:
        tupla_retorno=tupla_retorno + (tupla[2],)
    if tupla[3]%2==0:
        tupla_retorno= tupla_retorno + (tupla[3],)
    return tupla_retorno#Start your python function here