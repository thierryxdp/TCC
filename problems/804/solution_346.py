#Start your python function here

def filtra_pares(x,y,w,z):
    """kkk"""
    pa = x%2
    pb = y%2
    pc = w%2
    pd = z%2
    
    if pa==0:
        return x
    if pa==0 and pb==0:
        return x , y
    if pa==0 and pb==0 and pc==0:
        return x , y , w
    if pa==0 and pb==0 and pc==0 and pd==0:
        return x , y , w , z