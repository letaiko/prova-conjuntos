#Jordan Vieira da Silva, Leonardo Figueiredo Morona, Letícia Aiko Takiguti dos Santos - 2B BCC
with open("entrada1.txt", "r") as arquivo: #prof, pra abrir os outros arquivos de entrada é só trocar "entrada1" pelo nome do txt
  linha = arquivo.readlines()

numeroMax = int(linha[0].replace("\n", ""))

for i in range(1, ((numeroMax*3)+1), 3):
    operacao = linha[i].replace("\n", "").replace(",", "")
    conj1 = set(linha[i+1].replace("\n", "").split(","))
    conj2 = set(linha[i+2].replace("\n", "").split(","))
    if operacao == "I":
      print(f"\nInterseção: Conjunto 1 {conj1}, Conjunto 2 {conj2}. Resultado: ", conj1.intersection(conj2))
    elif operacao == "U":
      print(f"\nUnião: Conjunto 1 {conj1}, Conjunto 2 {conj2}. Resultado: ", conj1.union(conj2))
    elif operacao == "D":
      print(f"\nDiferença: Conjunto 1 {conj1}, Conjunto 2 {conj2}. Resultado: ", conj1.difference(conj2))
    elif operacao == "C":
      print(f"\nProduto Cartesiano: Conjunto 1 {conj1}, Conjunto 2 {conj2}. Resultado: ", end="")
      for i in conj1:
        for j in conj2:
          print(f"({i},{j}), ", end="")
