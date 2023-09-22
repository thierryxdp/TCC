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
  string3 = ""
  string2 = retira_pontuacao(string)
  lista = string2.lower().split()
  for i in range(-1, -len(lista)-1, -1):
    if i == -len(lista):
      string3 = string3 + lista[i]
    else:
       string3 = string3 + lista[i] + " "
  return string3