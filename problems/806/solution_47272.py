def colisao(ret1,ret2):
    xe1, ye1, xd1, yd1 = ret1
    xe2, ye2,  xd2, yd2 = ret2
    if ((min(xe1,xd1)<=xd2<=max(xe1,xd1) or min(xe1,xd1)<=xe2<=max(xe1,xd1))and max(ye1,yd1)<ye2 or max(ye1,yd1)<yd2)and ((min(ye1,yd1)<=ye2<=max(ye1,yd1) or min(ye1,yd1)<=yd2<=max(ye1,yd1))and(max(xe1,xd1)>xd2 or max(xe1,xd1)>xe2)):
        return True
    else:
        return False