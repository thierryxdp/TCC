def freq_palavras(frases):
    d1 = {}
    frases0 = str.split(frases,' ' )
    d1[frases0[0]] = 0
    d1[frases0[1]] = 0
    d1[frases0[2]] = 0
    d1[frases0[3]] = 0
    d1[frases0[4]] = 0
    d1[frases0[5]] = 0
    d1[frases0[6]] = 0
    if len(frases0) > 7:
     d1[frases0[7]] = 0
     d1[frases0[8]] = 0
     d1[frases0[9]] = 0
     d1[frases0[10]] = 0
     d1[frases0[11]] = 0
     d1[frases0[0]] = d1[frases0[0]] + 1
     d1[frases0[1]] = d1[frases0[1]] + 1
     d1[frases0[2]] = d1[frases0[2]] + 1
     d1[frases0[3]] = d1[frases0[3]] + 1
     d1[frases0[4]] = d1[frases0[4]] + 1
     d1[frases0[5]] = d1[frases0[5]] + 1
     d1[frases0[6]] = d1[frases0[6]] + 1
     d1[frases0[7]] = d1[frases0[7]] + 1
     d1[frases0[8]] = d1[frases0[8]] + 1
     d1[frases0[9]] = d1[frases0[9]] + 1
     d1[frases0[10]] = d1[frases0[10]] + 1
     d1[frases0[11]] = d1[frases0[11]] + 1
    return d1