def retira_pontuacao(F):
    x0 = F.strip('!')
    x1 = x0.strip('?')
    x2 = x1.strip('.')
    x3 = x2.strip(',')
    x4 = x3.strip('-')
    x5 = x4.replace(',','')
    x6 = x5.replace('-',' ')
    
    return str(x6) + str(" ")