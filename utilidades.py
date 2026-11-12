def ler_texto(mensagem, vazio=False):
    while True:
        texto = input(mensagem).strip()
        if texto != "" or vazio:
            return texto
        print("O texto não pode ficar vazio.")


def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem).strip())
            if minimo is not None and valor < minimo:
                print(f"O mínimo é {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"O máximo é {maximo}.")
                continue
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")


def linha(caractere="-", tamanho=40):
    return caractere * tamanho


if __name__ == "__main__":
    print(linha("=", 30))
    nome = ler_texto("Teste nome (obrigatório): ")
    idade = ler_inteiro("Teste idade (0 a 120): ", 0, 120)
    print(f"Resultado: {nome}, {idade} anos")
    print(linha("-", 30))
