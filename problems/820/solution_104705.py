#Função que recebe duas strings e um numero e retorna a posição em que houve
#a ocorrencia respectiva da segunda string ao numero dado e retorn um inteiro
#caso a quantidade de ocorrencias nao seja maior que o numero dado
#str, str, int -> int
def posLetra(string, letra, num):
    txt = list(string)
    i=0
    pos=[]
    while i < len(txt):
    	if txt[i].lower() == letra.lower():
               pos.append(i)
        i+=1
    if len(pos) < num:
        return -1
    else:
    	return pos[num-1]