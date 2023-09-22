def lingua_p(palavra):
    for vogal in "AEIOUaeiouáéíóú":
        palavra=str.replace(palavra,vogal,vogal+"p"+vogal)
    return palavra