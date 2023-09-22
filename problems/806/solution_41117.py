def colisao(ret1,ret2):
    
    xe1, ye1, xd1, yd1 = ret1
    xe2, ye2,  xd2, yd2 = ret2
    if colisao([6,5,8,7],[6,2,7,5]):
        print(True)
    if colisao([1,4,9,7],[8,7,9,8]):
        print(True)
    else:
        print(False)