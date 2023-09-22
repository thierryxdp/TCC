def lingua_p(plvr):
    palv_p=''
    vgs='aáàãeéèiíoóòõuúù'
    l=0
    while l<len(plvr):
        if plvr[l] in vgs:
            palv_p+=plvr[l]+'p'+plvr[l]
        else:
            palv_p+=plvr[l] 
        l+=1
    return palv_p