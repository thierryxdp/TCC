# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    """Recebe os valores dimencionais de um colchão e uma porta
    	e returna True se o colchao passa pela porta e false se não
        list, float, float -> bool"""
    hc = medida[0]
    lc = medida[1]
    cc = medida[2]
    menor = min(H,L)
    maior = max(H,L)
    passa = False    
    if(hc<=menor and lc<=menor) or(hc<=menor and lc<=maior) or (hc<=maior and lc<=menor):
        passa = True
    elif(lc<=menor and cc<=menor) or(lc<=menor and cc<=maior) or (lc<=maior and cc<=menor):
        passa = True
    elif(hc<=menor and cc<=menor) or(hc<=menor and cc<=maior) or (hc<=maior and cc<=menor):
        passa = True    
    return passa