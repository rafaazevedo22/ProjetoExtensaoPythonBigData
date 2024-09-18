import pandas as pd

# Carregar a planilha
file_path = 'clientes.xlsx'  # Substitua pelo caminho do seu arquivo
df = pd.read_excel(file_path)

# Exibir as primeiras linhas do DataFrame para verificar o carregamento
print("Dados originais:")
print(df.head())

# Organizar os dados: ordenar por Código do cliente e Dia de cotação
df_sorted = df.sort_values(by=['Código do Cliente', 'Data de Cotação'])

# Remover duplicatas baseadas em Código do cliente, mantendo a primeira ocorrência
df_unique = df_sorted.drop_duplicates(subset=['Código do Cliente'], keep='first')

# Verificar e tratar valores ausentes (opcional)
df_cleaned = df_unique.fillna('Não informado')  # Substitui valores ausentes por 'Não informado'

# Exibir as primeiras linhas do DataFrame limpo e organizado
print("\nDados organizados e limpos:")
print(df_cleaned.head())

# Salvar o DataFrame organizado em um novo arquivo Excel
output_path = 'clientes_organizados.xlsx'
df_cleaned.to_excel(output_path, index=False)

print(f"\nPlanilha organizada salva em: {output_path}")
