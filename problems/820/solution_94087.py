def posLetra(frase,letra,n):
      """Recebe uma string, uma letra e a ocorrência desejada da letra e retorna a posição da string que acontece tal ocorrência"""
      x=0
      for i in range(len(frase)):
            if frase[i]==letra:
                  x+=1
            if x==n:
                  return i
      if x<n:
            return -1