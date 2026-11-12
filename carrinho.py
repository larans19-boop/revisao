def subtotal_item(preco, quantidade=1):
    return preco * quantidade


def aplicar_cupom(total, cupom):
    cupons = {
        "PROMO10": 10,
        "VOLTAASAULAS": 15,
        "BLACK25": 25
    }
    codigo = cupom.strip().upper()
    percentual = cupons.get(codigo, 0)
    novo_total = total * (1 - percentual / 100)
    return novo_total, percentual


def calcular_frete(total, gratis_acima=200.0, valor=25.0):
    if total >= gratis_acima:
        return 0.0
    return valor


def valor_parcela(total, parcelas=1):
    if parcelas <= 6:
        return total / parcelas
    return (total * (1 + 0.02 * parcelas)) / parcelas


if __name__ == "__main__":
    print("=== LOJA VIRTUAL ===")
    subtotal_geral = 0.0

    while True:
        produto = input("Produto (Enter para fechar o carrinho): ").strip()
        if produto == "":
            break

        while True:
            try:
                preco = float(input("Preço: R$ ").strip().replace(",", "."))
                if preco > 0:
                    break
                print("Digite um valor maior que zero.")
            except ValueError:
                print("Digite um preço válido.")

        while True:
            try:
                qtd = int(input("Quantidade: ").strip())
                if qtd > 0:
                    break
                print("Digite um valor maior que zero.")
            except ValueError:
                print("Digite uma quantidade inteira válida.")

        sub = subtotal_item(preco, qtd)
        subtotal_geral += sub
        print(f"{qtd} x {produto} = R$ {sub:.2f} (carrinho: R$ {subtotal_geral:.2f})")

    cupom_digitado = input("Cupom de desconto (Enter se não tiver): ").strip()
    total_com_desconto, perc = aplicar_cupom(subtotal_geral, cupom_digitado)
    if cupom_digitado != "" and perc == 0:
        print("Cupom inválido. Nenhum desconto aplicado.")

    desconto_reais = subtotal_geral - total_com_desconto
    frete = calcular_frete(total_com_desconto)
    total_final = total_com_desconto + frete

    while True:
        try:
            parcelas = int(input("Em quantas parcelas (1 a 12)? ").strip())
            if 1 <= parcelas <= 12:
                break
            print("Escolha entre 1 e 12 parcelas.")
        except ValueError:
            print("Digite um número inteiro entre 1 e 12.")

    parcela_valor = valor_parcela(total_final, parcelas)

    print("\n=== NOTA ===")
    print(f"Subtotal:  R$ {subtotal_geral:.2f}")
    print(f"Desconto:  {perc}% (R$ {desconto_reais:.2f})")
    print(f"Frete:     R$ {frete:.2f}")
    print(f"Total:     R$ {total_final:.2f}")
    print(f"Pagamento: {parcelas} x R$ {parcela_valor:.2f}")
