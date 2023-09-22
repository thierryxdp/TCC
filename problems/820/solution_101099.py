def posLetra(frase, letra, num=0):
    '''Faça uma função posLetra que recebe como entrada uma 
  string, uma letra, e um n umero que indica a ocorrencia 
  desejada da letra (1 para primeira ocorrencia, 2 para segunda, etc).
  Sua função deve retornarem que posição da string aquela 
  ocorrencia da letra esta. Caso exista menos ocorrencias 
  da letra do que a ocorrencia pedida, 
  a funcao deve retornar -1. str,str,int - > int
    '''
    x = num
    tem = False
    while x < len(frase) and not tem:
        if frase[x] == letra:
            tem = True
        else:
            x = x + 1
    if tem and num<=len(letra):
        return x
    elif num<=len(letra):
        return x
    else:
        return -1