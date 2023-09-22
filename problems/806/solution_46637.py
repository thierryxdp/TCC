def colisao(ret1, ret2):
        '''
        A funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
        coordenadas dos vertices inferior esquerdo e superior direito do primeiro retângulo e do segundo 
        retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
        tuple, tuple --> bool
        '''
        '''
        Nomenclatura das variaveis:
        X ou Y (eixos), I ou S (inferior ou superior)
        E ou D (esquerda ou direita), 1 ou 2 (retângulo 1 ou 2)
        '''
    
        XIE1, YIE1, XSD1, YSD1 = ret1
        XIE2, YIE2, XSD2, YSD2 = ret2
        
        if ((XSD1<XIE2) or (YSD2<YIE1)):
                return False
        else:
                return True