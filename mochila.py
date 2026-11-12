print("=== MOCHILA DE CAMPING ===")
print("Digite os itens. Para terminar, digite FIM.")

nomes = []
pesos = []
limite = 15.0

while True:
    nome = input("Item: ").strip()
    if nome.upper() == "FIM":
        break
    if not nome:
        print("Digite o nome do item.")
        continue

    while True:
        peso_str = input("Peso (kg): ").strip().replace(",", ".")
        try:
            peso = float(peso_str)
            if peso <= 0:
                print("O peso deve ser maior que zero.")
            else:
                break
        except ValueError:
            print("Digite um número, por exemplo 1.5")

    nomes.append(nome)
    pesos.append(peso)

    total_atual = sum(pesos)
    if total_atual > limite:
        print(f"Atenção: a mochila já tem {total_atual:.1f} kg (limite 15 kg)!")

print("\n=== RESUMO ===")
if len(nomes) == 0:
    print("A mochila está vazia.")
else:
    for i in range(len(nomes)):
        print(f"{i + 1}. {nomes[i]:<20} {pesos[i]:.1f} kg")

    total = sum(pesos)
    media = total / len(pesos)
    maior_peso = max(pesos)
    idx_maior = pesos.index(maior_peso)

    print(f"\nItens: {len(nomes)}")
    print(f"Peso total: {total:.1f} kg")
    print(f"Peso médio: {media:.2f} kg")
    print(f"Item mais pesado: {nomes[idx_maior]} ({maior_peso:.1f} kg)")

    if total > limite:
        print(f"Tire {total - limite:.1f} kg da mochila para ficar dentro do limite.")
    else:
        print(f"Ainda cabem {limite - total:.1f} kg na mochila.")
