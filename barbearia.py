import pandas as pd

# Load: carregar os dados do CSV para um DataFrame
df = pd.read_csv("clientes_barbearia.csv")

# Exibir os primeiros registros para confirmar
print("Dados carregados:")
print(df.head())

# Converter para lista de dicionários (cada linha vira um dict)
users = df.to_dict(orient="records")

print("\nLista de usuários carregada:")
for user in users:
    print(user)

# Gerar mensagens automáticas para cada cliente
for user in users:
    news = f"{user['Nome']}, seu corte está agendado! Compareça no horário marcado."
    print(news)
    if "news" not in user:
        user["news"] = []
    user["news"].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })
