print("=== EXCURSÃO DA ESCOLA ===")

while True:
    try:
        qtd_turmas = int(input("Quantas turmas vão participar? "))
        if qtd_turmas > 0:
            break
        print("Digite um número inteiro maior que zero.")
    except ValueError:
        print("Digite um número inteiro válido.")

total_alunos = 0
maior_turma = ""
maior_inscritos = -1

for i in range(1, qtd_turmas + 1):
    while True:
        nome_turma = input(f"Nome da turma {i}: ").strip()
        if nome_turma:
            break
        print("O nome da turma não pode ficar vazio.")

    while True:
        try:
            inscritos = int(input(f"Inscritos na turma {nome_turma}: "))
            if inscritos >= 0:
                break
            print("Digite um número inteiro (0 ou mais).")
        except ValueError:
            print("Digite um número inteiro (0 ou mais).")

    total_alunos += inscritos
    if inscritos > maior_inscritos:
        maior_inscritos = inscritos
        maior_turma = nome_turma

professores = (total_alunos + 14) // 15 if total_alunos > 0 else 0
total_pessoas = total_alunos + professores
onibus = (total_pessoas + 43) // 44 if total_pessoas > 0 else 0
lugares_sobrando = (onibus * 44) - total_pessoas
custo_total = onibus * 1800.00
valor_por_aluno = custo_total / total_alunos if total_alunos > 0 else 0.0

print("\n=== RESUMO ===")
print(f"Alunos: {total_alunos}")
print(f"Professores acompanhantes: {professores}")
print(f"Total de pessoas: {total_pessoas}")
print(f"Ônibus necessários: {onibus} (sobram {lugares_sobrando} lugares)")
print(f"Custo total: R$ {custo_total:.2f}")
print(f"Valor por aluno: R$ {valor_por_aluno:.2f}")
print(f"Turma com mais inscritos: {maior_turma} ({maior_inscritos} alunos)")
