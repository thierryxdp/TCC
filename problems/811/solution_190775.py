def colchao(a,b,c,H,L):
    '''funcao que retorna se e possivel um colchao passar pela porta apartir dos parametros (medidas=a.b.c) que sao os parametros do colchao e (H,L) que sao a altura e largura da porta
    list,int,int->bool'''
    (a,b,c)=[a,b,c]
    if 2*(ab+ac)<H*L:
        return 'True'
    else:
        return 'False'