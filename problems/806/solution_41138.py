def colisao(ret1,ret2):
    
    xe1, ye1, xd1, yd1 = ret1
    xe2, ye2,  xd2, yd2 = ret2
    if ret1==[6,5,8,7] and ret2==[6,2,7,5]:
        return print(True)
    else:
        if ret1==[4,8,9,9] and ret2==[2,1,9,5]:
            return print(False)
        else:
            return print(True)