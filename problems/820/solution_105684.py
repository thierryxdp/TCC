#Função que recebe como entrada uma string, uma letra e um numero,que indica a ocorrencia desejada da letra na string e retorna a posição da ocorrencia da letra na lista; str,str,str = int
def posLetra(texto,letra,numero):
    posicao = 0
    contador = [0,]
    if letra not in texto or numero > texto.count(letra):
        return -1
    while posicao < len(texto):
          if letra in texto:
              pos = str.find(texto,letra)
              contador = contador + [pos]
              texto= str.replace(texto,letra,'a',1)
          posicao = posicao +1
          
    return contador[numero]