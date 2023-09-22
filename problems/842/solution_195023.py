#Start your python function here
def iden(pontuacao):
    nome1= pontuacao[0]
    nome2= pontuacao [1]
    t1= pontuacao[2]
    t2= pontuacao [3]
    t_1= pontuacao [6]
    t_2= pontuacao [7]
def jogo1 (a,b):
    if t1(pontuacao(a))==t2(pontuacao(b)):
       return (1,1)
    elif t1(pontuacao(a))>=t2(pontuacao(b)):
         return (3,0)
    else:
          return (0,3)
def jogo2 (a,b):
    if t1(pontuacao(a))==t2(pontuacao(b)):
       return (1,1)
    elif t1(pontuacao(a))>=t2(pontuacao(b)):
         return (3,0)
    else:
          return (0,3)
def pontos_por_time(a):
    return {nome1(iden(a)):jogo1(iden(a)),nome2(iden(a)):jogo2(iden(a))}