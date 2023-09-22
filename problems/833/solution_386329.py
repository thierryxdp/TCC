def RangeNumListas (num):
    '''
       Função que recebe um número positivo e
       inteiro (num) e retorna uma lista com
       num listas, cada uma contendo um elemento.
       Os elementos serão distribuídos em ordem
       crescente do 0 até (num-1);
       int -> list
    '''
    lista_ele_de_num=[]
    for i in range(num):
        lista_ele_de_num+=[[i]]
    return lista_ele_de_num