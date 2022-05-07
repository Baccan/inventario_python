# Construa um sistema de inventario capaz de
# cadastrar um produto,
# alterar o preço,
# aplicar depreciação,
# remover o produto,
# buscar um produto e
# gerar relatorio de inventario.

from helpers import *

cadastrarProdutos = True

txtInputNomeProduto = "Insira o nome do produto: "
txtInputPreco = "Insira o preço do produto: "
txtInputTempoDepreciacao = "Insira o tempo de depreciação do produto em anos: "
txtInputValorResidual = "Insira apenas o número do valor residual do produto em porcentagem: "
txtInputCadastrarMais = "Deseja cadastrar mais produtos (S ou N)? "
txtInputManipularProdutos = "Deseja alterar (A) e aplicar depreciação, remover (R) ou buscar (B) algum produto? Ou sair (Q) do sistema? "


print("Olá! Vamos cadastras seus produtos.")
while cadastrarProdutos:
    nomeProduto = input(txtInputNomeProduto).title()
    while not nomeProduto:
        nomeProduto = input(txtInputNomeProduto).title()

    preco = float(input(txtInputPreco))
    while preco < 0:
        print("Preço do produto não pode ser menor que 0! O preço foi corrigido e zerado: ")
        preco = 0

    tempoDepreciacao = float(input(txtInputTempoDepreciacao))
    while tempoDepreciacao < 0:
        print("Tempo de depreciação do produto não pode ser menor que 0! O valor foi corrigido e zerado: ")
        tempoDepreciacao = 0

    valorResidual = float(input(txtInputValorResidual))
    while valorResidual < 0:
        print("Valor residual do produto não pode ser menor que 0! O valor foi corrigido e zerado: ")
        valorResidual = 0

    cadastrarProduto(nomeProduto, preco, tempoDepreciacao, valorResidual)

    cadastrarMais = input(txtInputCadastrarMais).upper()
    while cadastrarMais != "S" and cadastrarMais != "N":
        print("Valor inválido!")
        cadastrarMais = input(txtInputCadastrarMais).upper()

    if(cadastrarMais == "N"):
        cadastrarProdutos = False


print("Confira a lista de produtos cadastrados:\n")
gerarRelatorioProdutos()

continuarSistema = True

while continuarSistema == True:
    if(not produtos or not isinstance(produtos, list) or produtos == []):
        print("Nenhum produto encontrado! Reunicie o sistema!")
        quit()

    manipularProdutos = input(txtInputManipularProdutos).upper()
    while manipularProdutos != "A" and manipularProdutos != "R" and manipularProdutos != "B" and manipularProdutos != "Q":
        print(manipularProdutos)
        manipularProdutos = input(txtInputManipularProdutos).upper()

    if(manipularProdutos == "Q"):
        print("Relatório: ")
        gerarRelatorioProdutos()
        quit()

    if(manipularProdutos == "B"):
        valorAbuscar = input(
            "Digite o valor de deseja buscar em um produto: ").title()
        valoresEncontrados = buscarProdutos(valorAbuscar)

        if valoresEncontrados:
            index = 0
            for produto in valoresEncontrados:
                print(f"\nID: {index}")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: {produto['preco']}")
                print(f"Tempo de Depreciacao: {produto['tempoDepreciacao']}")
                print(f"Valor residual: {produto['valorResidual']}")
                if produto['valorDepreciacao']:
                    print(
                        f"Valor de depreciação: {produto['valorDepreciacao']}")
                index += 1

    if(manipularProdutos == "A"):
        idProdutoAlteracao = int(
            input("Digite o ID do produto que deseja alterar: "))
        alterarProduto(idProdutoAlteracao)

    if(manipularProdutos == "R"):
        idProdutoAlteracao = int(
            input("Digite o ID do produto que deseja remover: "))
        removerProduto(idProdutoAlteracao)
