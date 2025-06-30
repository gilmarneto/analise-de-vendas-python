# data inicial: 20/06/2025
# datas de atualização: 20/23/24/06/2025

# importar bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import locale, os
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # para formato brasileiro de moeda

# Limpar tela do terminal
os.system('cls')

# 1. Criar um arquivo CSV ou TXT com dados como:
# Produto -> OK

# Caminho do arquivo
caminho = "PROJETAO_01/arquivos/"
arquivo = "dados.txt"

# Função(Calcular o faturamento por produto (preço × quantidade vendida))
def faturamento_produto(produto, vendidos, preco):
    faturamento_por_produto = {}
    for num_prod in range(len(produto)):
        nome_produto = produto[num_prod]
        valor_faturamento = vendidos[num_prod]*preco[num_prod]
        if nome_produto in faturamento_por_produto:
            faturamento_por_produto[nome_produto] += valor_faturamento
        else:
            faturamento_por_produto[nome_produto] = valor_faturamento

    print("---------- Faturamento por Produto ----------")

    for prod, val in faturamento_por_produto.items():
            print(f"Produto: {prod:<20} | Valor total: {locale.currency(round(val, 2), grouping=True)}")
    
    print("---------------------------------------------")
    mostrar_grafico = input("Deseja exibir gráfico, (s=sim | n=não)? ")

    if mostrar_grafico == "s":
        # montagem do gráfico
        # OBS: MATPLOTLIB USA LISTA E NÃO DICIONÁRIO DIRETO
        # Vamos separar o produto do valor e colocar em uma lista
        # produto(keys)
        produtos = list(faturamento_por_produto.keys())
        # valor(values)
        valores = list(faturamento_por_produto.values()) 
        plt.bar(produtos, valores, color="blue")
        plt.title("Faturamento por Produto")
        plt.ylabel("Valor total(R$)")
        plt.xlabel("Produto")
        plt.xticks(rotation=45, ha='right')  # Gira os nomes
        plt.tight_layout() # Layout automático
        plt.show()

# Função(Listar os itens encalhados (estoque alto, vendas baixas))
def produtos_encalhados(produto, estoque, vendidos):
    print("------ Produtos com baixa venda ------")
    for num_prod in range(len(produto)):
        media_encalhados = estoque[num_prod] / vendidos[num_prod]
        if media_encalhados > 3.0:
            print(f">>> {produto[num_prod]}")

# Função(Encontrar os produtos mais vendidos)
def produtos_mais_vendidos(produto, vendidos, minimo=21):
        print("------ Produtos mais vendidos ------")
        for num_prod in range(len(produto)):
            if vendidos[num_prod] > minimo:
                print(f">>> {produto[num_prod]} -> Qtde. vendida: {vendidos[num_prod]}")

# Função(Fazer um ranking de categorias com maior faturamento)
# OBS: ORDENAR NO MAIOR PARA O MENOR (MELHORIA)
def faturamento_categoria(categoria, vendidos, preco):
    #print(categoria, " / ", vendidos, " / ", preco)
    # 1º iterar o valor de cada lista de atributo
    faturamento_por_categoria = {}
    for num_categrorias in range(len(categoria)):
        
        cate = categoria[num_categrorias]
        vend = vendidos[num_categrorias]
        prec = preco[num_categrorias]
        tot_vend_prod = vend*prec # nesse caso eu tenho o valor faturado por produto vendido

        if cate in faturamento_por_categoria:
            faturamento_por_categoria[cate]["faturamento_categoria"] += tot_vend_prod
        else:
            faturamento_por_categoria[cate] = {"faturamento_categoria":tot_vend_prod}

    # dicionario para lista
    lista_faturamento_categoria = list(map(lambda item: {"categoria":item[0], "faturamento_categoria":item[1]['faturamento_categoria']}, faturamento_por_categoria.items()))
    ordenar_faturamento_categoria = sorted(lista_faturamento_categoria, key=lambda fc: fc['faturamento_categoria'], reverse=True)

    print("------ Rancking - Faturamento por Categoria ------")
    for i, items in enumerate(ordenar_faturamento_categoria, start=1):
        print(f"{i}º {items['categoria']:<10} | Valor total: {locale.currency(round(items['faturamento_categoria'], 2), grouping=True)}")
    print("--------------------------------------------------")
# Com o arquivo criado vamos chamá-lo
try:
    dados = np.genfromtxt(caminho+arquivo, delimiter=",", names=True, encoding="utf-8", dtype=None)
    produto = dados["Produto"]
    categoria = dados["Categoria"]
    estoque = dados["Estoque"]
    vendidos = dados["Vendidos"]
    preco = dados["Preco"]
    # print(produto,categoria,estoque,vendidos,preco)
    # Criando menu de opções
    print("--------------- Menu de Opções ---------------")
    print("----------------------------------------------")
    print(">>> 1 ---> Faturamento por produto")
    print(">>> 2 ---> Listar produtos encalhados")
    print(">>> 3 ---> Listar produtos mais vendidos")
    print(">>> 4 ---> Listar faturamento por categorias")
    opcao = int(input("\ninforme a opção desejada: "))
    print("----------------------------------------------")
    match opcao:
        case 1:
            faturamento_produto(produto, vendidos, preco)
        case 2:
            produtos_encalhados(produto, estoque, vendidos)
        case 3:
            produtos_mais_vendidos(produto, vendidos)
        case 4:
            faturamento_categoria(categoria, vendidos, preco)
        case _:
            print("Comando inválido")
    
except FileNotFoundError:
    print("Arquivo não encontrado!!")
except Exception as e:
    print(f"ERRO! {e}")

# OBS: SHIFT+TAB, PARA VOLTAR TABULAÇÃO