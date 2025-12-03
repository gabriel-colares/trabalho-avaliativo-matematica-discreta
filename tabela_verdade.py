from itertools import product
from parser_proposicional import parse_expr, get_variables

def _resolver_implicacao(a, b):
    return (not a) or b

def avaliar(expr, valores):
    # converte operadores simples
    expr_py = expr.replace("->", "IMPLICA")
    expr_py = expr_py.replace("<->", "EQUIV")

    # substitui variáveis pelos valores
    for k, v in valores.items():
        expr_py = expr_py.replace(k, str(v))

    # substitui palavras temporárias
    expr_py = expr_py.replace("IMPLICA", "_resolver_implicacao")
    expr_py = expr_py.replace("EQUIV", "==")

    return eval(expr_py)

def tabela_verdade(premissas, conclusao):
    todas = premissas + [conclusao]
    vars = sorted(set().union(*[get_variables(x) for x in todas]))

    print("\nTabela-verdade:\n", vars, " | Resultado")

    valido_em_todos = True

    for bits in product([False, True], repeat=len(vars)):
        vals = dict(zip(vars, bits))

        premissas_val = all(avaliar(p, vals) for p in premissas)
        concl_val = avaliar(conclusao, vals)

        print(vals, " | ", premissas_val, "->", concl_val)

        if premissas_val and not concl_val:
            valido_em_todos = False

    return valido_em_todos
