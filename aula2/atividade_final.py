
#Criando tupla
linguagens_tupla = ('Java', 'Python', 'Golang', 'C#', 'Javascript')

#Tupla transformada em lista
linguagens_lista = list(linguagens_tupla)
print("Tupla transformada em lista")

print(type(linguagens_lista))

# Adicionando dois elementos com extend
linguagens_lista.extend(["Ruby", "Malbolge"])
print("Lista com dois dados adicionados")
print(linguagens_lista)


linguagens_lista.pop(0)


print("Lista com JAVA removido")
print(linguagens_lista)

print("Primeiro elemento:")
print(linguagens_lista[0])


print("Quantidade de  elementos:")
print(len(linguagens_lista))



dicionario = {
    "Nome": "Matheus",
    "Idade": 25,
    "Profissão": "Garoto do Programa"
}

print(dicionario["Nome"])
