import random
from datetime import datetime
import utilidades

print(utilidades.linha("=", 40))
print("SORTEIO DE BRINDES - FEIRA DE CIÊNCIAS")
print(utilidades.linha("=", 40))
print("Digite os nomes dos participantes (Enter vazio para terminar).")

participantes = []
participantes_lower = []

while True:
    num = len(participantes) + 1
    nome = utilidades.ler_texto(f"Participante {num}: ", vazio=True)
    if nome == "":
        break
    if nome.lower() in participantes_lower:
        print(f"{nome} já está na lista.")
    else:
        participantes.append(nome)
        participantes_lower.append(nome.lower())

if len(participantes) == 0:
    print("Nenhum participante cadastrado. Sorteio encerrado.")
else:
    qtd_brindes = utilidades.ler_inteiro(
        f"Quantos brindes (1 a {len(participantes)})? ",
        minimo=1,
        maximo=len(participantes)
    )

    brindes = []
    for i in range(1, qtd_brindes + 1):
        brinde = utilidades.ler_texto(f"Brinde {i}: ")
        brindes.append(brinde)

    ganhadores = random.sample(participantes, qtd_brindes)
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M")

    print("\n" + utilidades.linha("-", 40))
    print(f"Sorteio realizado em {agora}")
    print(f"{len(participantes)} participantes, {qtd_brindes} brindes")
    print(utilidades.linha("-", 40))

    for i in range(qtd_brindes):
        print(f"{brindes[i]:<20} -> {ganhadores[i]}")
