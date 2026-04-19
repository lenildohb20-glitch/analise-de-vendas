import pandas as pd
import matplotlib.pyplot as plt

# 1. Ler dados
df = pd.read_csv('dados.csv')

# 2. Mostrar dados
print("=== DADOS ===")
print(df)

# 3. Verificar dados faltantes
print("\n=== DADOS FALTANTES ===")
print(df.isnull().sum())

# 4. Converter coluna de data
df['data'] = pd.to_datetime(df['data'])

# 5. Criar coluna faturamento
df['faturamento'] = df['quantidade'] * df['preco']

# 6. Análise por produto
faturamento_produto = df.groupby('produto')['faturamento'].sum()

# 7. Análise por categoria
faturamento_categoria = df.groupby('categoria')['faturamento'].sum()

# 8. Produto mais vendido
mais_vendido = df.groupby('produto')['quantidade'].sum().idxmax()

print("\n=== RESULTADOS ===")
print("Produto mais vendido:", mais_vendido)

print("\nFaturamento por produto:")
print(faturamento_produto)

print("\nFaturamento por categoria:")
print(faturamento_categoria)

# 9. Gráfico de barras
faturamento_produto.plot(kind='bar', title='Faturamento por Produto')
plt.show()

# 10. Gráfico de pizza
faturamento_categoria.plot(kind='pie', autopct='%1.1f%%', title='Faturamento por Categoria')
plt.show()