time = input("Digite seu time: ")

match time:
    case "Corinthians":
        print("Você é um Timão!")
    case "Bahia":
        print("Você é Esquadrão!")
    case "Gremio":
        print("Você é imortal!")
    case _:
        print("Quem não é não se mete")

