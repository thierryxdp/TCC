def posLetra(frase,letra,ocorrencia):
   '''função que recebe uma string, uma letra e um numero e retorna 
   em que posição da string a ocorrencia da letra está, e retorna
   -1 se houver menos ocorrencias do que o numero informado.
   str, str, int -> int'''
    lista=list(frase)
    contador = lista.count(letra)
    
    if contador >= ocorrencia:
        substitui = str.replace(frase,letra,'&',ocorrencia-1)
        return str.find(substitui,letra,0,-1)
    else:
        return -1