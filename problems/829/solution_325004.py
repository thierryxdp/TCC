def  soma_h ( n ):
#Faça uma função chamada *soma_h* para calcular e retornar o valor H com N termos onde N é inteiro e dado com entrada.
    soma  =  0
    para  i  no  intervalo ( 1 , n + 1 ):
        soma  +=  1 / i
    soma  =  redondo ( soma , 2 )
    devolver  soma