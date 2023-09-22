#Start your python function here
def filtra_pares(tupla):
    """ recebe duas datas no formato ”DD/MM/AAAA”, sendo a segunda maior que a primeira, e calcula o total de dias passados entre uma data e outra.
        
        Parameters:
            data1 = primeira data escolhida (data mais antiga)
            data2 = sgunda data escolhida (data mais recente)
        
        Testes:
            diff_datas("02/03/1982", "01/02/1983") = 334
            diff_datas("19/06/2002", "03/01/2021") = 6769
            diff_datas("02/01/2021", "03/01/2021") = 1

        Returns:
            Total de dias encontrado entre as datas escolhidas
            str, str -> int.
    """
    a, b, c, d = tupla
    resultado = 0,
    if  a % 2 == 0:
        a = (a,)
        resultado = resultado + a
    if  b % 2 == 0:
        b = (b,)
        resultado = resultado + b
    if  c % 2 == 0:
        c = (c,)
        resultado = resultado + c
    if  d % 2 == 0:
            d = (d,)
            resultado = resultado + d
    return resultado [1:]