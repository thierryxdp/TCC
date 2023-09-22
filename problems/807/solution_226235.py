def conta_frases(fra):
    text=str.replace(fra,"...",".")
    return text.count("?")+text.count("!")+text.count(".")