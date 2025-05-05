import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV
df = pd.read_csv('ecommerce_estatistica.csv')

# Visualizar os primeiros dados
print(df.head())

# Ver estrutura e estatísticas
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Converter coluna 'Qtd_Vendidos' para numérica (caso tenha textos)
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce')

# Gráfico de Histograma
plt.figure(figsize=(8,5))
plt.hist(df['Preço'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuição de Preços')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.show()

# Gráfico de Dispersão
plt.figure(figsize=(8,5))
plt.scatter(df['Preço'], df['Nota'], alpha=0.5)
plt.title('Relação entre Preço e Nota')
plt.xlabel('Preço')
plt.ylabel('Nota')
plt.show()

# Mapa de Calor (Correlação)
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Mapa de Calor - Correlação entre Variáveis')
plt.show()

# Gráfico de Barras (ex: por temporada)
df['Temporada'].value_counts().plot(kind='bar', color='orange', figsize=(8,5))
plt.title('Quantidade de Produtos por Temporada')
plt.xlabel('Temporada')
plt.ylabel('Quantidade')
plt.show()

# Gráfico de Pizza (ex: por marca)
df['Marca'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
plt.title('Distribuição por Marca')
plt.ylabel('')
plt.show()

# Gráfico de Densidade (ex: Nota)
sns.kdeplot(df['Nota'], fill=True, color='green')
plt.title('Distribuição de Densidade das Notas')
plt.xlabel('Nota')
plt.show()

# Gráfico de Regressão (Preço vs Qtd_Vendidos)
sns.lmplot(x='Preço', y='Qtd_Vendidos', data=df)
plt.title('Regressão Linear - Preço vs Quantidade Vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')
plt.show()
