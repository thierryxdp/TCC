def colchao(medidas,H,L):
    
    colchao1=medidas[0]*medidas[1]
    colchao2=medidas[0]*medidas[2]
    colchao3=medidas[1]*medidas[2]
    porta= H*L
    
    if (porta>colchao1)or(porta>colchao2)or(porta>colchao3):
        return 1==2
    if(porta<=colchao1)or(porta<=colchao2)or(porta<=colchao3):
        return 1==1