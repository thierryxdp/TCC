def filtra_pares(x0,x1,x2,x3):
     '''Função que retorna uma tupla igual aos valores pares da tupla de entrada, na mesma ordem;
     entrada: int, int, int, int;
     saída: int;
     '''
     sopares = ()
     if ((x0%2)==0):
        par0 = x0 #variável para quando o primeiro elemento é par;
     elif ((x1%2)==0):
        par1=x1 #variável para quando o segundo elemento é par;
     elif ((x2%2)==0):
        par2=x2 #variável para quando o terceiro elemento é par;
     elif ((x3%2)==0):
        par3=x3 #variável para quando o quarto elemento é par;
     else:
        par0=() #variável para quando o primeiro elemento é ímpar;
        par1=() #variável para quando o segundo elemento é ímpar;
        par2=() #variável para quando o terceiro elemento é ímpar;
        par3=() #variável para quando o quarto elemento é ímpar;
    return sopares + par0 + par1 + par2 + par3