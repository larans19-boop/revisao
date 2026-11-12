def formatar_duracao(minutos):
    horas = minutos // 60
    resto = minutos % 60
    if horas > 0:
        return f"{horas}h{resto:02d}min"
    return f"{resto}min"


def tempo_total(duracoes):
    soma = 0
    for d in duracoes:
        soma += d
    return soma


def dias_para_terminar(total_minutos, minutos_por_dia=120):
    return (total_minutos + minutos_por_dia - 1) // minutos_por_dia


def classificar_maratona(total_minutos):
    if total_minutos < 300:
        return "Leve"
    elif total_minutos <= 900:
        return "Média"
    return "Intensa"


if __name__ == "__main__":
    print("=== MARATONA DE SÉRIE ===")
    while True:
        serie = input("Nome da série: ").strip()
        if serie:
            break
        print("Digite o nome da série.")

    while True:
        try:
            temporadas = int(input("Quantas temporadas? ").strip())
            if temporadas > 0:
                break
            print("Digite um número maior que zero.")
        except ValueError:
            print("Digite um número inteiro válido.")

    duracoes_temporadas = []

    for t in range(1, temporadas + 1):
        while True:
            try:
                eps = int(input(f"Temporada {t} - número de episódios: ").strip())
                if eps > 0:
                    break
                print("Digite um número maior que zero.")
            except ValueError:
                print("Digite um número inteiro válido.")

        while True:
            try:
                dur_ep = int(input(f"Temporada {t} - duração média do episódio (min): ").strip())
                if dur_ep > 0:
                    break
                print("Digite um número maior que zero.")
            except ValueError:
                print("Digite um número inteiro válido.")

        duracoes_temporadas.append(eps * dur_ep)

    print(f"\n=== {serie.upper()} ===")
    for i, dur in enumerate(duracoes_temporadas, start=1):
        print(f"Temporada {i}: {formatar_duracao(dur)}")

    total = tempo_total(duracoes_temporadas)
    classificacao = classificar_maratona(total)
    print(f"Total: {formatar_duracao(total)} ({classificacao})")

    while True:
        try:
            min_dia = int(input("\nQuantos minutos por dia você pode assistir? ").strip())
            if min_dia > 0:
                break
            print("Digite um número maior que zero.")
        except ValueError:
            print("Digite um número inteiro válido.")

    dias_usuario = dias_para_terminar(total, min_dia)
    dias_padrao = dias_para_terminar(total)

    print(f"Você termina {serie} em {dias_usuario} dias.")
    print(f"Com 2 horas por dia (padrão), seriam {dias_padrao} dias.")
