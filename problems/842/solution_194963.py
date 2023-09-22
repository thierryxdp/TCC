def traducao_rnaM(x):
    trinca={'UUU':'Phe','CUU':'Leu','UUA':'Leu','AAG':'Lisina','UCU':'Ser','UAU':'Tyr','CAA':'Gln'}
    a=x[0:3]
    b=x[3:6]
    c=x[6:]
    return trinca[a]+'-'+trinca[b]+'-'+trinca[c]
    




def listas(l1,l2):
    return [l1[0],l2[0],l1[1],l2[1],l1[2],l2[2]]



def colchao(D,H,L):
    a=D[0]
    b=D[1]
    c=D[2]
    if a<=L and b<=H:
        return True
    else:
        return False

def pontos_por_time(Lista):
    Jogo_ida=Lista[0]
    Jogo_volta=Lista[1]
    n_time1=Jogo_ida[0]
    n_time2=Jogo_ida[1]
    gida=Jogo_ida[2]
    gvolta=Jogo_volta[2]
    a1=gida[0]
    a2=gida[1]
    b1=gvolta[0]
    b2=gvolta[1]
    if a1>a2 and b1>b2:
        pont1=6
        pont2=0
    elif a1>a2 and b1==b2 or a1==b2 and b1>b2:
        pont1=4
        pont2=1
    elif a1==a2 and b1==b2:
        pont1=2
        pont2=2
    elif a1<a2 and b1>b2 or a1>a2 and b1<b2:
        pont1=3
        pont2=3
    elif a1==a2 and b1<b2 or a1<a2 and b1==b2:
        pont1=1
        pont2=4
    else:
        pont1=0
        pont2=6
        
    return {n_time1:pont1,n_time2:pont2}