"""Função que verifica se um numero é primo a partir de um numero qualque dado como entrada da fução
int->bool"""
def primo(numero):
    x=[]
    for i in range(2,numero):
        if numero%i==0:
            list.append(x,i)
	if len(x) > 0:
        return False
    else:
        return True