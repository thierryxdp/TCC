def posLetra(frase, letra, num=0):
    '''Faça uma função posLetra que recebe como entrada uma 
  string, uma letra, e um n umero que indica a ocorrencia 
  desejada da letra (1 para primeira ocorrencia, 2 para segunda, etc).
  Sua função deve retornar em que posi ̧c ̃ao da string aquela ocorrˆencia da letra est ́a. Caso exista menos ocorrˆencias da letra do que
a ocorrˆencia pedida, a fun ̧c ̃ao deve retornar -1.
    '''
    ix = num
    tem = False
    while ix < len(frase) and not tem:
        if frase[ix] == letra:
            tem = True
        else:
            ix = ix + 1
            if tem and num<=len(letra):
                  return ix
            elif num<=len(letra):
                  return ix
            else:
                  return -1