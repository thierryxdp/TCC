def retira_pontuacao(frase):
    '''dada uma frase(frase), retorna uma string correspondente a frase, com todas as pontuacoes substituidas por espaco; str -> str'''
    A = str.replace(frase, '-',' ')
    B = str.replace(A, ',',' ')
    C = str.replace(B, ':',' ')
    D = str.replace(C, ';',' ')
    E = str.replace(D, '.',' ')
    F = str.replace(E, '!',' ')
    G = str.replace(F, '?',' ')
    return G

def  inverte(string):
  posinicial = -1
  string2 = retira_pontuacao(string)
  string2.lower()
  for i in range(1, len(string2)-1):
    if string2[-i] == " ":
      string3 = string3 + string2[posinicial: -i]+ " "
      posinicial = -i

  return string3