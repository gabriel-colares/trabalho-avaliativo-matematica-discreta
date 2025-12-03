from itertools import product
from parser_proposicional import parse_expr, get_variables

def avaliar(expr, valores):
    expr_py = parse_expr(expr)
    for k, v in valores.items():
        expr_py = expr_py.replace(k, str(v))
    return eval(expr_py)

def tabela_verdade(premissas, conclusao):
    todas = premissas + [conclusao]
    vars_list = []
    for x in todas:
        for v in get_variables(x):
            if v not in vars_list:
                vars_list.append(v)
    vars = sorted(vars_list)
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
