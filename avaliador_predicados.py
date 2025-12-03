from itertools import product
from parser_predicados import parse_predicado

def avaliar_predicados(premissas, conclusao, dominio):
    pred_prem = [parse_predicado(p) for p in premissas]
    pred_conc = parse_predicado(conclusao)
    for interpretacao in product([True, False], repeat=len(dominio)):
        if all(interpretacao[0] for _ in pred_prem) and not interpretacao[0]:
            return False
    return True
