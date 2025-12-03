def identificar_forma(premissas, conclusao):
    if len(premissas) == 2 and "->" in premissas[0] and premissas[1] in premissas[0]:
        return "Modus Ponens"
    if len(premissas) == 2 and "->" in premissas[0] and "~" + premissas[1] in premissas[0]:
        return "Modus Tollens"
    return "Forma não reconhecida"
