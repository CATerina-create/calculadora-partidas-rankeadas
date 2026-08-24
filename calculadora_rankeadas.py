def calcular_rankeada(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo_vitorias, nivel


continuar = "s"

while continuar == "s":
    vitorias = int(input("Digite a quantidade de vitórias: "))
    derrotas = int(input("Digite a quantidade de derrotas: "))

    saldo, nivel = calcular_rankeada(vitorias, derrotas)

    print(f"O Herói tem de saldo de {saldo} está no nível de {nivel}")

    continuar = input("Deseja continuar? (s/n): ").lower()