def posLetra(frase, letra, n):
    '''Retorna em que posição da string aquela ocorrência da letra está.
    Caso exista menos ocorrências da letra do que a ocorrência pedida,
    a função deve retornar -1.
    frase ->str '''
    frase = 'palavra'
    letra = 'a'
    n=3
    i=0
    p=0
      while i<len(frase):
        if letra in frase[i]:
            p = p + 1
  
      return i