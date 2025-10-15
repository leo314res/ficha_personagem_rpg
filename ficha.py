import random
from dados import silab, racas, classe, origem, mentor, eventos, habilidade, name_atrib, fraqueza

# Função geradora de nomes
def ger_name():
    num_silab = random.randint(2,3) # Utiliza duas ou três sílabas

    name = ''
    for i in range(num_silab):
        name += random.choice(silab) # Escolhe as sílabas aleatóriamente
    return name.capitalize()

name_end = ger_name()

# Função geradora de atributos
def atrib():

    # Gera os valores dos atributos
    gerar = {
        valor: random.randint(1, 30) # Valor mínimo e máximo
        for valor in name_atrib
    }
    return gerar

att_gerado = atrib()

# Função geradora da ficha completa de personagem
def ficha():
    nome = ger_name()
    raca = random.choice(racas)
    classes = random.choice(classe)
    orig = random.choice(origem)
    ment = random.choice(mentor)
    event = random.choice(eventos)
    hab = random.choice(habilidade)
    fraq = random.choice(fraqueza)
    atributo = atrib()

    print("-" * 30)
    print(f"""FICHA DE PERSONAGEM
{"-" * 30}
Nome: {nome}
Raça: {raca}
Classe: {classes}
{"-" * 30}
{nome}, o {classes} da raça {raca}, nasceu em {orig}.
Criado por {ment}, ele {event}.
Desde então, {hab}, moldando quem ele é hoje.
{"-" * 30}
FRAQUEZA: {fraq}
{"-" * 30}
ATRIBUTOS:""")

    # Imprime os atributos linha por linha
    for name, valor in atributo.items():
        print("{}: {}".format(name,valor))

if __name__ == "__main__":
    while True:
        ficha()
        
        while True:  # Loop para validar a resposta
            resposta = input("\nDeseja fazer outro personagem? \n1 - SIM \n2 - NÃO \nResposta: ").strip()
            if resposta == '1':
                break 
            elif resposta == '2':
                print("Encerrando o programa...")
                exit()
            else:
                print("Entrada inválida! Digite apenas 1, 2 ou 3.\n")
