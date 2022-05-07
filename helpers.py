produtos = []


def calcDepreciacao(preco: float, tempoDepreciacao: float, valorResidual: float):
    return (preco - (preco * (valorResidual/100))) / tempoDepreciacao


def cadastrarProduto(nome: str, preco: float, tempoDepreciacao: float, valorResidual: float):
    global produtos

    produtos.append({
        'nome': nome,
        'preco': preco,
        'tempoDepreciacao': tempoDepreciacao,
        'valorResidual': valorResidual,
        'valorDepreciacao': None
    })


def gerarRelatorioProdutos():
    global produtos

    if(not produtos or not isinstance(produtos, list) or produtos == []):
        print("Não há produtos cadastrados!")
        return

    index = 0
    for produto in produtos:
        print(f"\nID: {index}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: {produto['preco']}")
        print(f"Tempo de Depreciacao: {produto['tempoDepreciacao']}")
        print(f"Valor residual: {produto['valorResidual']}")
        if produto['valorDepreciacao']:
            print(f"Valor de depreciação: {produto['valorDepreciacao']}")
        index += 1

    print("Fim do relatório\n")


def buscarProdutos(valorAbuscar, alteracao=False):
    if(not produtos or not isinstance(produtos, list) or produtos == []):
        print("Não há produtos cadastrados!")
        return []

    valoresEncontrados = []

    index = 0
    for produto in produtos:
        if(alteracao):
            if (int(valorAbuscar) == index):
                valoresEncontrados.append(produto)
                break
        else:
            if (valorAbuscar == index or
                    valorAbuscar in str(produto['nome']) or
                    valorAbuscar in str(produto['preco']) or
                    valorAbuscar in str(produto['tempoDepreciacao']) or
                    valorAbuscar in str(produto['valorResidual'])
                ):
                valoresEncontrados.append(produto)
        index += 1

    if not valoresEncontrados:
        print(
            f"Não foram encontrados produtos com o valor infromado ({valorAbuscar})!")
        return []

    print("Fim da busca por produtos\n")
    return valoresEncontrados


def alterarProduto(idProdutoAlteracao: int):
    global produtos

    txtInputCadastrarMais = "Deseja cadastrar mais produtos (S ou N)? "
    txtInputOqueDesejaAlterar = "O que deseja alterar no produto? (Nome - 1, preço - 2, Tempo de Depreciação - 3, Valor Residual - 4): "
    txtInputAplicarDeprecicacao = "Deseja aplicar depreciação (S ou N)? "

    produtoAserAlterado = buscarProdutos(idProdutoAlteracao, True)

    if(not produtoAserAlterado or not isinstance(produtoAserAlterado, list) or produtoAserAlterado == []):
        return

    oqueDesejaAlterar = int(input(txtInputOqueDesejaAlterar))
    while (oqueDesejaAlterar != 1 and
           oqueDesejaAlterar != 2 and
           oqueDesejaAlterar != 3 and
           oqueDesejaAlterar != 4
           ):
        print("Valor inválido!")
        oqueDesejaAlterar = int(input(txtInputCadastrarMais))

    novoValor = input("Digite o novo valor: ")

    match oqueDesejaAlterar:
        case 1:  # nome
            produtos[idProdutoAlteracao]['nome'] = novoValor.title()
        case 2:  # preco
            produtos[idProdutoAlteracao]['preco'] = float(novoValor)
        case 3:  # tempoDepreciacao
            produtos[idProdutoAlteracao]['tempoDepreciacao'] = float(novoValor)
        case 4:  # valorResidual
            produtos[idProdutoAlteracao]['valorResidual'] = float(novoValor)

    aplicarDepreciacao = input(txtInputAplicarDeprecicacao).upper()
    while aplicarDepreciacao != "S" and aplicarDepreciacao != "N":
        print("Valor inválido!")
        aplicarDepreciacao = input(txtInputAplicarDeprecicacao).upper()

    if(aplicarDepreciacao == "N"):
        return

    produtos[idProdutoAlteracao]['valorDepreciacao'] = calcDepreciacao(
        produtos[idProdutoAlteracao]['preco'],
        produtos[idProdutoAlteracao]['tempoDepreciacao'],
        produtos[idProdutoAlteracao]['valorResidual'])

    produtoAlterado = produtos[idProdutoAlteracao]

    print(f"\nProduto alterado:")
    print(f"ID: {produtos.index(produtoAlterado)}")
    print(f"Nome: {produtoAlterado['nome']}")
    print(f"Preço: {produtoAlterado['preco']}")
    print(f"Tempo de Depreciacao: {produtoAlterado['tempoDepreciacao']}")
    print(f"Valor residual: {produtoAlterado['valorResidual']}")
    print(f"Valor de depreciação: {produtoAlterado['valorDepreciacao']}")


def removerProduto(idProdutoRemocao: int):
    global produtos

    index = 0
    for produto in produtos:
        if idProdutoRemocao == index:
            del produtos[idProdutoRemocao]
            print(f"Produto {idProdutoRemocao} removido")
            return
        index += 1

    print(f"Nenhum produto encontrado com ID {idProdutoRemocao} para remoção")
