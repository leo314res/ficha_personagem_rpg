# ⚔️ Gerador de Fichas de Personagem RPG

 Um gerador de fichas de personagem para jogos de RPG de fantasia, desenvolvido em Python. Ele conjura personagens completos e aleatórios com atributos, história inicial, raça, classe, e até mesmo seus pontos fracos, oferecendo uma experiência de *role-playing* imediata e inspiradora.

---

## 🧙‍♂️ Recursos de Criação e Magia

- **Nomes Aleatórios Únicos:** Geração dinâmica de nomes a partir de sílabas predefinidas, garantindo originalidade.
- **Identidade Completa:** Escolha mágica e aleatória de **Raça**, **Classe**, **Origem** e um **Mentor** influente.
- **Atributos do Herói:** Definição dos valores (entre 1 e 30) para 10 atributos cruciais, como Força, Inteligência, Carisma e a sempre vital Sorte.
- **Jornada e Personalidade:** Seleção de **Eventos de Vida** marcantes, **Habilidades Especiais** (dons) e **Fraquezas** (maldições ou medos) que moldam a alma do personagem.
- **Criação em Série:** Capacidade de forjar múltiplos destinos em uma única sessão.

---

## 🛠️ O Motor de Criação (Estrutura Técnica)

O projeto é construído em torno das seguintes funções e listas de dados, que são o coração da aleatoriedade:

- `ger_name()`: Função que costura sílabas (`silab`) para dar vida a um nome.
- `atrib()`: Distribui os 10 valores aleatórios para os atributos definidos em `name_atrib`.
- `ficha()`: A função mestra que orquestra a seleção de todos os elementos e imprime o pergaminho final (a ficha).
- **Dados:**
    - `racas`: O catálogo de povos e espécies.
    - `classe`: As vocações e caminhos de poder.
    - `origem`: Lugares de nascimento e criação.
    - `mentor`: Figuras que passaram ensinamentos importantes.
    - `eventos`: Momentos que definiram o passado do herói.
    - `habilidade`: Poderes ou talentos inatos.
    - `fraqueza`: Vulnerabilidades e falhas de caráter.

---

## 📜 Guia de Invocação (Como Usar)

1. **Requisito Mínimo:** Confirme que possui o **Python 3.12** ou superior instalado em seu sistema.
2. **Obtenha o Código:** Clone o repositório ou faça o download dos arquivos do projeto.
3. **Execute o Encanto:** Abra seu terminal no diretório do projeto e execute o arquivo principal:

```bash
python ficha.py
Siga o Destino: O programa irá guiá-lo no terminal para gerar novas fichas.
Para Encerrar: Simplesmente selecione a opção NÃO quando perguntado sobre criar outro personagem.

Exemplo de Ficha Gerada:
------------------------------
FICHA DE PERSONAGEM
------------------------------
Nome: Kalumi
Raça: Elfo
Classe: Mago
------------------------------
Kalumi, o Mago da raça Elfo, nasceu em uma floresta sombria.
Criado por um velho sábio, ele descobriu poderes mágicos.
Desde então, aprendeu a manejar a espada, moldando quem ele é hoje.
------------------------------
FRAQUEZA: medo de altura
------------------------------
ATRIBUTOS:
Força: 18
Destreza: 24
Constituição: 12
Agilidade: 22
Inteligência: 27
Sabedoria: 20
Carisma: 15
Vontade: 19
Percepção: 23
Sorte: 16

💻 Tecnologias e Conceitos
Python 3.12 (a base de toda a magia) e Vscode (o livro de edição).

Manipulação eficiente de listas e funções para gerenciar os dados do mundo.

Uso de estruturas de repetição e condicionais para orquestrar a lógica de criação.

✒️ Autor: Leonardo Pires

Este projeto é um estudo prático de Python, transformando linhas de código em narrativas e personagens.