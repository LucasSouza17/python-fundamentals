# Declaração
nome_completo = "Lucas Fernando de Souza"

nome_completo_aspas = """
Lucas
Fernando
de
Souza
"""

nome_completo_quebra = "Lucas \
Fernando de Souza"

nome = "Lucas"
sobrenome = "Fernando de Souza"

# Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Lucas" + "Fernando")
print("Nome completo (4a forma):" + "Lucas", "Fernando")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))

# Métodos

# upper()
print("Formatando para tudo maiúsculo:", nome_completo.upper())

# lower()
print("Formatando para tudo minúsculo:", nome_completo.lower())

# Retornando cada letra
print("Retornando primeira letra do nome:", nome_completo[0])

# count("")
print("Qntd letras do nome completo:", nome_completo.count(""))

# count(letra) - Encontra quantas letras "A a Z" existem na string
print("Qntd letras a's que existem no nome completo:", nome_completo.count("a"))

# find(letra) - Busca e retorna o índice onde a letra A está
print("Buscar primeira indice da primeira evidência da letra A:", nome_completo.find("a"))

# enconde() - Codifica a string em bytes
print("Codificar string para bytes:", nome.encode())

# decode() - Decodifica algo que já está em bytes
print("Decodificar bytes para strings:", nome.encode().decode())

# replace() - Substitui letras por letras exemplo, substituir toda letra b pela letra a
print("Substitui letra A por letra B:", nome_completo.replace("a", "b"))

# join() - A cada caracteres ele adiciona um outro por exemplo l-u-c-a-s
print("Adiciona um traço entre os caracteres:", "-".join(nome_completo))

# split() - Divide a string em um dicionário dependendo do parâmetro
print("Separa o nome em um dicionário atraves dos espaços:", nome_completo.split(" "))

# strip() - Remove tudo que ta ou no começo e no fim que correponde ao parametro string enviado
# rstrip() - Remove tudo que está a esquerda
# lstrip() - Remove tudo que está a direita
nome_com_erro = 'xLucasx'
print("Verifica se há um X antes ou depois da string e remove:", nome_com_erro.strip("x"))

# startswith() - Valida se a string começa com um nome especifico ou palavra ou letra
print("Verifica se o nome começa com Luc:", nome_completo.startswith("Luc"))

# endswith() - Valida se a string termina com um nome especifico ou palavra ou letra
print("Verifica se o nome começa com As:", nome_completo.startswith("as"))

# Verifica se um conjunto de string existe em uma palavra ou texto
print("Verifica se Fernando existe no nome completo:", "Fernando" in nome_completo)




