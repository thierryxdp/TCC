def filtra_pares(e0,e1,e2,e3):
    '''Função que retorna uma tupla igual aos valores pares da tupla de entrada, na mesma ordem;
    entrada: int, int, int, int;
    saída: tuple;
    '''
    sopares= ()
    if (e0 % 2 == 0):
        par0= (e0,) #variável para quando o primeiro elemento é par;
    else:
        par0=()
    if (e1 % 2 == 0):
        par1= (e1,) #variável para quando o segundo elemento é par;
    else:
        par1=()
    if (e2 % 2 == 0):
        par2= (e2,) #variável para quando o terceiro elemento é par;
    else:
        par2=()
    if (e3 % 2 == 0):
        par3= (e3,) #variável para quando o quarto elemento é par;
    else:
        par3= ()
    return sopares + par0 + par1 + par2 + par3#Start your python function here