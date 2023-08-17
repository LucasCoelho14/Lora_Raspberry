import json

#criação de um pacote json imaginário para um teste
dados = {
    "nome": "Joao",
    "idade": 30,
    "cidade": "Sao Paulo"
}
# Tratamento do pacote para usá-lo como string
dados_analisados = json.dumps(dados)
lista_bytes = bytes(dados_analisados, 'utf-8')

#leitura e impressão do tamho da lista
print(lista_bytes)
print("\n")
print(len(lista_bytes))