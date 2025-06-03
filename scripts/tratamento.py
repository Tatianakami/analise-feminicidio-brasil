import pandas as pd

# Dicionário para converter código de estado para nome
mapa_estados = {
    11: 'Rondônia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Pará',
    16: 'Amapá', 17: 'Tocantins', 21: 'Maranhão', 22: 'Piauí', 23: 'Ceará',
    24: 'Rio Grande do Norte', 25: 'Paraíba', 26: 'Pernambuco', 27: 'Alagoas',
    28: 'Sergipe', 29: 'Bahia', 31: 'Minas Gerais', 32: 'Espírito Santo',
    33: 'Rio de Janeiro', 35: 'São Paulo', 41: 'Paraná', 42: 'Santa Catarina',
    43: 'Rio Grande do Sul', 50: 'Mato Grosso do Sul', 51: 'Mato Grosso',
    52: 'Goiás', 53: 'Distrito Federal'
}

# Carregar dados brutos
df = pd.read_csv('dados/homicidios-mulheres.csv', sep=';', encoding='utf-8')

# Criar coluna com código de estado (dois primeiros dígitos da coluna 'cod')
df['cod_estado'] = df['cod'].astype(str).str[:2].astype(int)

# Mapear código para nome do estado
df['estado'] = df['cod_estado'].map(mapa_estados)

# Renomear colunas para ficar mais intuitivo
df.rename(columns={'período': 'Ano', 'valor': 'Taxa Feminicídio'}, inplace=True)

# Salvar arquivo tratado para análise e visualização
df.to_csv('dados/dados_tratados.csv', index=False, encoding='utf-8')

print("✅ Dados tratados salvos em 'dados/dados_tratados.csv'")



