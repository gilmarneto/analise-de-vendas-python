# 📊 Analisador de Vendas com Python

Este projeto foi desenvolvido para analisar dados de vendas de forma simples, usando Python. Ele carrega um arquivo `.txt` com informações de produtos e fornece relatórios úteis, além de gráficos automáticos com `matplotlib`.

---

## 🔍 Funcionalidades

- ✅ Faturamento por produto
- 🔄 Produtos encalhados (estoque alto vs. vendas baixas)
- 📈 Produtos mais vendidos
- 🏆 Ranking de categorias por faturamento
- 📊 Geração de gráfico de barras com os dados

---

## 📁 Estrutura do projeto
analise-de-vendas-python/
├── arquivos/
│ └── dados.txt
├── analisador_vendas.py
└── README.md

---

## 🧪 Exemplo do arquivo `dados.txt`

```txt
Produto,Categoria,Estoque,Vendidos,Preco
Notebook,Eletrônicos,10,4,3500.00
Fone de Ouvido,Acessórios,50,10,150.00
Smartphone,Eletrônicos,30,25,2100.00
```
---

▶️ Como executar
Instale as bibliotecas:

pip install numpy matplotlib
Execute o script no terminal:

Para abrir:
python analisador_vendas.py
Escolha uma das opções do menu interativo.
