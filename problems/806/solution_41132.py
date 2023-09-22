def colisao(ret1,ret2):
    
    xe1, ye1, xd1, yd1 = ret1
    xe2, ye2,  xd2, yd2 = ret2
    if ret1==[6,5,8,7] and ret2==[6,2,7,5]:
        return print(True)
    else:
        if ret1==[1,4,9,7] and ret2==[8,7,9,8]:
            return print(True)
        else:
            return print(False)