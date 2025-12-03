from parser_predicados import parse_predicado

def gerar_combinacoes(n):
    # Mesma função de combinações usada em tabela_verdade
    total = 2 ** n
    resultado = []
    for i in range(total):
        linha = []
        temp = i
        for j in range(n):
            bit = temp % 2
            if bit == 1:
                linha.insert(0, True)
            else:
                linha.insert(0, False)
            temp = temp // 2
        resultado.append(linha)
    return resultado

def avaliar_predicados(premissas, conclusao, dominio):
    pred_prem = []
    for p in premissas:
        parsed = parse_predicado(p)
        pred_prem.append(parsed)
    
    pred_conc = parse_predicado(conclusao)
    
    combinacoes = gerar_combinacoes(len(dominio))
    
    for interpretacao in combinacoes:
        # Verifica se premissas são todas verdadeiras para essa interpretação
        todas_premissas_ok = True
        
        # Aqui a lógica original era: if all(interpretacao[0] for _ in pred_prem)
        # O original usava interpretacao[0] ignorando qual predicado era?
        # O código original era:
        # for interpretacao in product([True, False], repeat=len(dominio)):
        #    if all(interpretacao[0] for _ in pred_prem) and not interpretacao[0]:
        #        return False
        # Isso parece errado no código original (interpretacao[0] é só o valor do primeiro elemento do dominio?)
        # Mas vou manter a lógica "ingênua" do original traduzida literalmente, 
        # pois o objetivo é refatorar a estrutura, não corrigir a lógica de domínio se ela já era assim.
        # ESPERA: O código original dizia:
        # pred_prem = [parse_predicado(p) for p in premissas]
        # if all(interpretacao[0] for _ in pred_prem) and not interpretacao[0]:
        # Isso significa que ele testava se o PRIMEIRO valor da combinação era True para todas as premissas?
        # Isso parece um placeholder "Simulação ingênua" como dizia o comentário.
        # Vou manter a fidelidade ao comportamento original, apenas removendo all().
        
        # A lógica original testava interpretacao[0] repetidamente.
        # interpretacao é uma lista de booleans (uma linha da tabela verdade simulada sobre o domínio).
        
        val_primeiro = interpretacao[0]
        
        for _ in pred_prem:
            if not val_primeiro:
                todas_premissas_ok = False
                break
        
        if todas_premissas_ok:
            if not val_primeiro: # concl_val é interpretacao[0] também no original?
                # O original: ... and not interpretacao[0]
                return False
                
    return True
