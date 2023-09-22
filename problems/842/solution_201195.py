def contatudo(d,t1,t2,gt1,gt2):
    if gt1<gt2 :
        d[t2] += 3
    if gt2< gt1:
        d[t1] += 3
    if gt2 == gt1:
        d[t2] +=1
        d[t1] +=1


def pontos_por_time(k):

    """ Essa função calcula os pontos de times dada uma lista com
       os dois times e o número de gols no jogo de ida e de volta.
       Assinatura: lista---> dicionario
       teste:
       pontos_por_time([['Cor', 'Fla',[1,0]],[ 'Fla', 'Cor', [2,2]]])== {'Cor': 4, 'Fla':1}
       pontos_por_time([['Palmeiras', 'Botafogo',[1,0]],[ 'Botafogo', 'Palmeiras', [2,2]]])=={'Palmeiras': 4, 'Botafogo': 1}
       pontos_por_time([['x', 'y',[20,0]],[ 'y', 'x', [20,2]]])=={'x': 3, 'y': 3}
       pontos_por_time([['x', 'y',[20,0]],[ 'x', 'y', [20,2]]])=={'x': 6, 'y': 0}

       """

    ida = k[0]
    volta= k[1]
    x = {ida[0]: 0 , ida[1]: 0}

    t1 = ida[0]
    t2 = ida[1]
    gt1= ida[2][0]
    gt2= ida[2][1]
    contatudo(x , t1, t2, gt1, gt2)

    t1 = volta[0]
    t2 = volta[1]
    gt1 = volta[2][0]
    gt2 = volta[2][1]
    contatudo(x, t1, t2, gt1, gt2)
    return x