

time = input("Digite seu time: ")

# if time == 'Corinthians':
#     print("Você é um Timão!")
# elif time == "Bahia":
#     print("Você é do Esquadrão")
# elif time == "Gremio":
#     print("Você é do Imortal")
# else:
#     print("Você não é um Timão!")


match time:
    case "Corinthians":
        print("Você é um Timão!")
    case "Bahia":
        print("Você é Esquadrão!")
    case "Gremio":
        print("Você é imortal!")
    case _:
        print("Quem não é não se mete")


