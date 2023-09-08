import json
# programa para ler e escrever arquivos para armazenamento 
# de dados em json
def reader(data=0):
    with open('data.json') as users_data:
        file = users_data.read()

x = reader()
print()