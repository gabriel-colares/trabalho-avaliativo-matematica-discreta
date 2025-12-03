from parser_proposicional import parse_expr, get_variables

def avaliar(expr, valores):
    expr_py = parse_expr(expr)
    for k in valores:
        v = valores[k]
        expr_py = expr_py.replace(k, str(v))
    return eval(expr_py)

def gerar_combinacoes(n):
    # Gera todas as combinações de True/False para n variáveis
    # Retorna uma lista de listas, ex: [[False, False], [False, True], ...]
    # Equivalente a itertools.product([False, True], repeat=n)
    total = 2 ** n
    resultado = []
    for i in range(total):
        linha = []
        temp = i
        for j in range(n):
            # Pega o último bit
            bit = temp % 2
            if bit == 1:
                linha.insert(0, True)
            else:
                linha.insert(0, False)
            temp = temp // 2
        resultado.append(linha)
    return resultado

def tabela_verdade(premissas, conclusao):
    todas = []
    for p in premissas:
        todas.append(p)
    todas.append(conclusao)

    vars_list = []
    for x in todas:
        vars_expr = get_variables(x)
        for v in vars_expr:
            existe = False
            for u in vars_list:
                if u == v:
                    existe = True
                    break
            if not existe:
                vars_list.append(v)
    
    vars = sorted(vars_list)
    
    header = ""
    for v in vars:
        if header != "":
            header = header + " | "
        header = header + v
    print("\nTabela-verdade:\n" + header + " | Resultado")

    valido_em_todos = True
    
    combinacoes = gerar_combinacoes(len(vars))

    for bits in combinacoes:
        vals = {}
        for i in range(len(vars)):
            vals[vars[i]] = bits[i]

        # Avaliar premissas manualmente sem all()
        premissas_val = True
        for p in premissas:
            valor_p = avaliar(p, vals)
            if not valor_p:
                premissas_val = False
                break
        
        concl_val = avaliar(conclusao, vals)

        # Montar string de valores para exibição
        vals_str = ""
        for i in range(len(vars)):
            v = vars[i]
            val = vals[v]
            s = "F"
            if val:
                s = "T"
            if vals_str != "":
                vals_str = vals_str + " | "
            vals_str = vals_str + s
        
        seta = "->"
        print(vals_str + " | " + str(premissas_val) + " " + seta + " " + str(concl_val))

        if premissas_val:
            if not concl_val:
                valido_em_todos = False

    return valido_em_todos
