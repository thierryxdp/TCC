def melhor_volta(matriz):
   
    volta_rapida_piloto=[]
    for linha in matriz:
        volta_rapida_piloto.append(min(linha))
    volt_mais_rap=min(volta_rapida_piloto)
    for c in matriz:
        if volt_mais_rap in c:
            pilot_mais_rapid=min(c)
  
    return pilot_mais_rapid,volt_mais_rap