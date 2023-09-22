def repetidos(lista):
   '''função que retorna quantas vezes o elemento 
   anterior de uma função é igual ao próximo
   valor de entrada: str
   valor de saída: int'''
	i = 1
    resposta = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            resposta = resposta + 1
        i = i + 1
    return resposta