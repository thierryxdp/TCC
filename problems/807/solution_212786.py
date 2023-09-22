def conta_frases(frases):
    if str.count(frases, '.')>0:
        return str.count(frases, '.' or ':' or '!' or '?' or '...', 0, len(frases))
    
    if str.count(frases, '!')>0 and str.count(frases, '.') == 0:
        return str.count(frases, '!')
  
    if str.count(frases, '?')>0 and str.count(frases, '.') == 0:
        return str.count(frases, '?')

    if str.count(frases, '...')>0 and str.count(frases, '.')>0 and str.count(frases, '?') and str.count(frases, '!'):
        return (str.count(frases, '...' and '.'))/2