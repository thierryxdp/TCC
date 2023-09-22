def bombom (dinheiro, preço) :
 ''' os parametros de entrada são do tipo (float,float).
 o valor de retorno é do tipo tupla (float,float)'''
return dinheiro//preço, dinheiro%preço
>>> bombom (10,3)
(3,1)