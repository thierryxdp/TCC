#Start your python function here
def pontoscor(gpc,gpf):
    if gpc>gpf:
        return 3
    if gpc<gpf:
        return 0
    else:
        return 1
    
def pontost1(gpf,gpc):
    if gpf>gpc:
        return 3
    if gpf<gpc:
        return 0
    else:
        return 1
    

def pontos_por_time(list):
    list=[jogoida,jogovolta]
    jogoida=[['Cormengo','Flaminthians',[gpc,gpf]]
    jogovolta=[['Flaminthians','Cormengo',[gpf,gpc]]
    dict={'Cormengo':pontoscor,
          'Flaminthians':pontosfla}