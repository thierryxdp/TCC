def melhor_volta ( matriz ) :
    melhor = 0
    menor_tempo = min ( matriz [ 0 ] )
    volta = matriz [melhor].index ( menor_tempo )
    for c1 in range ( len ( matriz ) ) :
        tempo = min ( matriz [ c1 ] )
        if ( tempo < menor_tempo ) :
            melhor = c1 
            menor_tempo = tempo
            volta = matriz [ melhor ].index ( menor_tempo )
    return ( menor_tempo , melhor , volta )