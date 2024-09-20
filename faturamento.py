#Total de vendas
vendas = [
    ('20/08/2024', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2024', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2024', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2024', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2024', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2024', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2024', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2024', 'ipad', 'prata', '128gb', 4000, 5000),
]
#Faturamento desejado
faturamento = 0
#Desmembramento e atribuição
for item in vendas:
    data, produto, cor, memoria, estoque, valor = item
    #Filtro produto e data
    if produto == 'iphone x' and data == '20/08/2024':
        faturamento += estoque * valor      
print('O faturamento total do produto {} na data {} é de {}'.format(vendas[0][1], vendas[0][0], faturamento))
#Produto mais vendido no dia 21/08/2020
produto_mais_vendido = ''
qtde_vendas = 0
for item in vendas:
    data, produto, cor, memoria, estoque, valor = item
    if data == '21/08/2024':
        if estoque > qtde_vendas:
            produto_mais_vendido = produto
            qtde_vendas = estoque
print('O produto mais vendido na data 21/08/2024 foi {} com {} unidades vendidas'.format(produto_mais_vendido, qtde_vendas))