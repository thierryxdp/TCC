def carros(passag,carro1,carron=5):
'''dado o numero de passageiros retorna a quantidade de carros com padrao 5 lugares ou nao)'''
return ceil(passag/(carro1+carron))