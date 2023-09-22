def lingua_p(palavra):
    txtP = ''
    txt = list(palavra)
    v = ['a','à','á','ã','â','e','é','è','ê','i','í','ì','î','o','ó','ò','õ','ô','u','ú','ù','û']
    for i in range(len(txt)):
        if txt[i] in v:
            pxp = txt[i] + 'p' + txt[i]
            txt[i] = str.replace(txt[i],txt[i],pxp)
    txtP = sum(txt)
    return txtP