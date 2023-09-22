def conta_frases(frases):
    """Essa função retorna quantas frases existem em um texto informado
    string --> int"""
    
    import re
    return len(re.split(".|?|!|...", frases))