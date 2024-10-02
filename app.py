campos_endereco = ["Plano-Piloto", "Asa sul", "SQS 210", "Bloco A", "Apartamento 404"]

# delimitador
delimitador = ";"

# juntar esses valores em uma única váriavel
endereco = delimitador.join(campos_endereco)

# exibir a variável na tela 
print(f"Endereço: \n {endereco}.")