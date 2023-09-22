def colchao(medidas, H, L):
    import math    
    L=math.sqrt(H**2+L**2)
    c=math.sqrt((medidas[2]-L)/2)**2-((L/H)*10)**2
    n=c**2/(L/H)
    H2=n+(L/H)
    x=math.sin(numpy.degrees(h2/medidas[1]))
    if x>=0.656059 and x<=0.694658:
        return True