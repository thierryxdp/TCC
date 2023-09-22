def lingua_p(plvr):
    '''Recebe uma palavra e retorna sua tradução para a língua do P em minusculas
    	str -> str'''
    plvr = lower(plvr)
    
    plvr = plvr.replace('a', 'apa')
    plvr = plvr.replace('e', 'epe')
    plvr = plvr.replace('i', 'ipi')
    plvr = plvr.replace('o', 'opo')
    plvr = plvr.replace('u', 'upu')
    
    plvr = plvr.replace('á', 'ápá')
    plvr = plvr.replace('é', 'épé')
    plvr = plvr.replace('í', 'ípí')
    plvr = plvr.replace('ó', 'ópó')
    plvr = plvr.replace('ú', 'úpú')
    
    plvr = plvr.replace('à', 'àpà')
    plvr = plvr.replace('è', 'èpè')
    plvr = plvr.replace('ì', 'ìpì')
    plvr = plvr.replace('ò', 'òpò')
    plvr = plvr.replace('ù', 'ùpù')
    
    plvr = plvr.replace('â','âpâ')
    plvr = plvr.replace('ê','êpê')
    plvr = plvr.replace('î','îpî')
    plvr = plvr.replace('ô','ôpô')
    plvr = plvr.replace('û','ûpû')
    
    plvr = plvr.replace('ã','ãpã')
    plvr = plvr.replace('õ','õpõ')
    
    plvr = plvr.replace('ä','äpä')
    plvr = plvr.replace('ë','ëpë')
    plvr = plvr.replace('ï','ïpï')
    plvr = plvr.replace('ö','öpö')
    plvr = plvr.replace('ü','üpü')
    
    
    return plvr