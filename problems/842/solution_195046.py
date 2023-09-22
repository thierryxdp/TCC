def iden(pontuacao):
    tuplaA1= pontuacao[0]
    tuplaA2= pontuacao [1]
    tuplaB1= tuplaA1 [0]
    tuplaB2= tuplaA1 [1]
    tuplaB3= tuplaA1 [2]
    tuplaC1= tuplaA2 [0]
    tuplaC2= tuplaA2 [1]
    tuplaC3= tuplaA2 [2]
    tuplaD1= tuplaB3 [0]
    tuplaD2= tuplaB3 [1]
    tuplaE1= tuplaC3 [0]
    tuplaE2= tuplaC3 [1]
    nome1= tuplaB1
    nome2= tuplaB2
    nome_1= tuplaC1
    nome_2= tuplaC2
    t1= tuplaD1
    t2= tuplaD2
    t_1= tuplaE1
    t_2= tuplaE2
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
    return iden(a)