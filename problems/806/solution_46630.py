def colisao(ret1,ret2):
     valoresx1=(ret1[0],ret1[2])
     valoresy1=(ret1[1],ret1[3])
     valoresx2=(ret2[0],ret2[2])
     valoresy2=(ret2[1],ret2[3])
     if (valoresx1[0] not in range(valoresx2[0],valoresx2[1]+1)) and ((valoresx1[1]) not in range(valoresx2[0],valoresx2[1]+1)) or (valoresy1[0] not in range(valoresy2[0],valoresy2[1]+1)) and ((valoresy1[1]) not in range(valoresy2[0],valoresy2[1]+1)):
        return(False)
    else: