def filtra_pares(tupla):
    """Função que recebe uma tupla e retorna uma nova tupla só com os numeros pares.
       tuple (int, int, int, int) -> tuple"""
    tupla_nova= ()
    for elemento in tupla:
        if elemento % 2==0:
            tupla_nova= tupla_nova + (elemento,)
    return tupla_nova
#Start your python function here