def num_bombons(din,pre):
	"""Função pega o dinheiro disponível (din) e o preço dos bombons (pre)
	e retorna a parte inteira (operador: // ).
    float//float=int """
    bombons=din//pre
    return bombons

#teste 1
#din==2.5
#pre==1.5 
#bombons==1
print(num_bombons(2.5,1.5))

#teste 2
#din==3.1
#pre==1.5 
#bombons==2
print(num_bombons(3.1,1.5))