def colisao(ret1,ret2):
    '''calcula a colisão ou não entre 2 retângulos
    tuple, tuple --> bool'''
    
    EsqInf1x , EsqInf1y , DirSup1x , DirSup1y = ret1
    EsqInf2x , EsqInf2y , DirSup2x , DirSup2y = ret2
    
    if ( EsqInf2x>DirSup1x or EsqInf1x>DirSup2x ) and
       ( EsqInf2y>DirSup1y or EsqInf1y>DirSup2y ):
            return False
        else:
            return True