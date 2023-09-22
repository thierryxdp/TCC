def divide_num(n,x):
    '''retorna n/x; int, int -> float'''
def media_matriz(matriz):
    '''retorna a media e todos os numeros da matriz; list -> float'''
	n=len(matriz[0])
    l=len(matriz)
    soma=[]
    for x in range(len(matriz)):
   
        soma=soma.append(list(map(divide_num,matriz[x],n*[n])))
    media=round(sum(soma)/l,2)
    return media