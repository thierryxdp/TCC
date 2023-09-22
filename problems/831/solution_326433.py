def lingua_p(palavra):
    for vogal in "AEIOUaeiou":
        palavra=str.replacec(palavra,vogal,vogal+"p"+vogal)
    return palavra