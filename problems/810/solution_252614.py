def remocao_pontuacao(frase):
    """função que retorna a uma frase sem caracteres de pontuação"""
    a = str.replace(frase,',',' ')
    b = str.replace(a,'.',' ') 
    c = str.replace(b,':',' ')
    d = str.replace(c,';',' ')
    e = str.replace(d,'-',' ')
    f = str.replace(e,'?',' ')
    g = str.replace(f,'!',' ')

    return g

def inverte(frase):
  """função que retorna a uma outra frase que contenha as
  mesmas palavras da frase de entrada na ordem inversa, sem letra 
  maiuscula e sem pontuação"""
  a = str.lower(remocao_pontuacao(frase))
  b= str.split(a)
  list.reverse(b)
  return str.join(' ',b)