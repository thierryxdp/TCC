def carros (pes, cap=5):
    if pes%cap!=0:
        result = pes // cap + 1
    else:
        result = pes // cap
    return result