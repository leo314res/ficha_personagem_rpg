# Sílabas que serão usadas na formação do nome
silab = ['ka', 'lo', 'mi', 'ra', 'tu', 'zen', 'vor', 'shi', 'dra', 'fen',
'gar', 'lu', 'no', 'pe', 'qua', 'rin', 'sol', 'tra', 'vek', 'yor',
'zan', 'bel', 'cor', 'di', 'fra', 'gis', 'hun', 'jek', 'kil', 'lom',
'mar', 'nir', 'osk', 'pra', 'qui', 'ron', 'sel', 'tur', 'uvi', 'val',
'wen', 'xor', 'yas', 'zim', 'bor', 'cha', 'den', 'el', 'fla', 'gro',
'hel', 'ian', 'jor', 'kir', 'lek', 'mor', 'nal', 'or', 'pol', 'rak',
'sen', 'tor', 'ul', 'ven', 'win', 'xer', 'yil', 'zur', 'bri', 'cla',
'dru', 'est', 'flo', 'gal', 'hil', 'jan', 'kro', 'lem', 'mur', 'nex',
'op', 'per', 'que', 'ril', 'sar', 'tes', 'und', 'vis', 'wer', 'xel',
'yun', 'zor', 'bil', 'cre', 'don', 'fas', 'gle', 'hor', 'iv', 'juv'
'aba', 'bem', 'cid', 'dor', 'evi', 'fry', 'gan', 'har', 'ika', 'jur',
'kel', 'lun', 'mip', 'nor', 'opa', 'pik', 'rav', 'sur', 'tek', 'uly',
'vys', 'wol', 'xan', 'yra', 'zenk', 'bry', 'cer', 'dai', 'emo', 'fal',
'gri', 'hur', 'ivn', 'jak', 'kor', 'lir', 'mun', 'nes', 'oru', 'paz',
'rel', 'sok', 'tiv', 'uma', 'vel', 'wic', 'xol', 'yer', 'zanq', 'zyl']

# Atributos do personagem
name_atrib = ['Força', 'Destreza', 'Constituição', 'Agilidade', 
'Inteligência', 'Sabedoria', 'Carisma', 'Vontade', 'Percepção', 'Sorte']

# Lista para fraqueza do personagem
fraqueza = ['medo de altura', 'avareza', 'orgulho excessivo', 'covardia', 'vício em álcool', 'ódio por uma raça específica', 'baixa resistência física', 'visão limitada', 'memória falha', 'dependência mágica', 'fobia de sangue', 'arrogância', 'lealdade cega', 'temperamento explosivo', 
'falta de empatia', 'ganância', 'insegurança constante', 'trauma de infância', 'desejo de vingança', 'impulsividade', 'egoísmo', 'lento em combate', 'supersticioso', 'fácil de manipular', 'fraco contra magia negra', 'susceptível a ilusões', 'dificuldade de confiar', 'fobia de fogo', 
'propenso a doenças', 'teimosia extrema', 'culpa persistente', 'medo de morrer', 'vulnerável à magia mental', 'ciúmes intensos', 'fraco sob pressão', 'susceptível à corrupção', 'ingenuidade', 'aversão à violência', 'voz fraca', 'medo de lugares fechados', 'perde o foco facilmente', 
'coragem irracional', 'dependência emocional', 'dificuldade em seguir ordens', 'fraco contra frio intenso', 'alergia mágica', 'instabilidade emocional', 'confia demais nos outros', 'tendência à solidão', 'susceptível a encantamentos', 'medo de fracassar'
]

# Para a escolha de raça
racas = ['Humano', 'Elfo', 'Anão', 'Orc', 'Goblin', 
'Gnomo', 'Halfling', 'Tiefling', 'Dragonborn', 'Meio-Elfo', 
'Meio-Orc', 'Kobold', 'Fada', 'Centauro', 'Minotauro', 'Troll', 
'Vampiro', 'Lich', 'Sereia', 'Anjo', 'Demoníaco', 'Licantropo', 'Gigante', 
'Elemental', 'Fantasma', 'Golem', 'Duende', 'Hobbit', 'Nômade', 'Satyr']

# Para a escolha de classe
classe = ['Guerreiro', 'Mago', 'Arqueiro', 'Ladrão', 'Paladino', 
'Clérigo', 'Bárbaro', 'Druida', 'Feiticeiro', 'Monge', 'Caçador', 'Necromante', 
'Bardo', 'Assassino', 'Cavaleiro', 'Alquimista', 'Xamã', 'Ladino Arcano', 
'Guerreiro Sagrado', 'Invocador', 'Sentinela', 'Elementalista', 'Gladiador', 
'Vidente', 'Pirata', 'Ninja', 'Templário', 'Corsário', 'Bruxo']

# Lista de origem para personagem
origem = ['uma vila pacífica', 'uma cidade movimentada', 'uma floresta sombria', 'uma montanha gelada', 'um castelo em ruínas', 'uma aldeia costeira', 'uma cidade subterrânea', 'uma ilha isolada', 'uma terra desértica', 'um reino esquecido', 'uma região infestada de monstros', 'uma planície ventosa',
'uma fortaleza militar', 'uma academia de magia', 'uma guilda de ladrões', 'uma biblioteca antiga', 'uma tribo nômade', 'uma caverna secreta', 'um templo abandonado', 'uma estrada perigosa', 'uma cidade flutuante', 'uma vila de pescadores', 'uma floresta encantada', 'uma região vulcânica', 
'um palácio em ruínas', 'uma torre arcana', 'uma mina abandonada', 'uma ponte antiga', 'um desfiladeiro', 'uma cidade portuária', 'uma vila de caçadores', 'uma colina verdejante', 'uma caverna gelada', 'uma aldeia fantasma', 'uma fortaleza escondida', 'um bosque místico', 
'uma pradaria aberta', 'uma mansão antiga', 'um templo secreto', 'uma vila de montanha', 'um laboratório escondido', 'uma cidade cercada por muralhas', 'uma praia deserta', 'um jardim abandonado', 'uma planície de gelo', 'uma torre do relâmpago', 'uma caverna de cristais', 'um bosque negro', 
'uma vila em ruínas', 'uma cidade industrial', 'um castelo de areia', 'uma aldeia nas nuvens', 'uma cidade soterrada', 'uma floresta de cogumelos gigantes', 'uma ilha misteriosa', 'uma ponte levadiça', 'uma vila escondida', 'uma torre de vigia', 'uma cidade subterrânea secreta', 'uma estrada antiga', 
'uma cidade mercante', 'uma planície cheia de ruínas', 'uma colina de cristais', 'uma vila de artistas', 'uma cidade abandonada pelo tempo', 'uma floresta de névoa', 'uma aldeia mágica', 'uma fortaleza de gelo', 'uma torre de observação', 'uma cidade costeira antiga', 'uma ponte suspensa', 
'uma vila de caçadores de monstros', 'uma cidade encravada em montanhas', 'uma aldeia de pastores', 'uma planície cheia de ruínas antigas', 'uma ilha de monstros', 'uma cidade cercada por lava', 'uma floresta de sombras', 'uma aldeia subterrânea', 'uma torre de magia negra', 'uma cidade das areias', 
'uma vila de pescadores fantasmas', 'uma planície de ventos cortantes', 'uma cidade abandonada no deserto', 'uma caverna de magma', 'uma ilha de cristal', 'uma cidade flutuante de magia', 'uma aldeia secreta', 'uma floresta de espíritos', 'uma cidade tomada por monstros', 'uma vila nas colinas', 
'uma torre esquecida', 'uma cidade perdida', 'uma floresta de cogumelos luminescentes', 'uma cidade das sombras', 'uma ilha escondida', 'uma cidade no topo da montanha', 'uma vila antiga', 
'uma caverna de gelo eterno', 'uma torre de relíquias', 'uma cidade portuária fantasma', 'uma aldeia de montanha isolada', 'uma floresta de neblina', 'uma planície selvagem']

# Lista para mentor do personagem
mentor = ['seu pai guerreiro', 'sua mãe arqueira', 'um velho sábio', 'uma guilda secreta', 'um mestre de espada', 'uma feiticeira misteriosa', 'um ancião da vila', 'seus irmãos aventureiros', 'uma ordem de clérigos', 'um caçador solitário', 'um alquimista excêntrico', 'um general aposentado', 
'um mentor fantasma', 'um espírito guardião', 'uma família nobre', 'um ladrão experiente', 'uma tribo guerreira', 'um mago errante', 'uma criatura mística', 'um professor rigoroso', 'uma guilda de mercenários', 'uma anciã da floresta', 'um bardo viajante', 'uma sacerdotisa arcana', 'um guerreiro lendário', 'um feiticeiro recluso', 'uma guilda de assassinos', 'uma guardiã do templo', 
'um alquimista ancião', 'uma criatura sábia', 'um mestre de arco', 'uma senhora do clã', 'um aprendiz prodígio', 'um cavaleiro errante', 'uma druida da floresta', 'um necromante reformado', 'um capitão da guarda', 'um espírito guardião da aldeia', 'uma maga do fogo', 'um professor de runas', 
'uma sacerdotisa misteriosa', 'um mestre de sombras', 'uma guerreira lendária', 'um arqueiro solitário', 'uma feiticeira das sombras', 'um mestre do caos', 'uma anciã guardiã', 'um mercador astuto', 'um capitão de navio', 'uma druida errante', 'um cavaleiro de luz', 'uma aprendiz de feiticeiro', 
'um mestre alquimista', 'uma guardiã do tempo', 'um bardo misterioso', 'uma sacerdotisa da lua', 'um caçador de monstros', 'uma anciã sábia', 'um mago do gelo', 'um guerreiro sombrio', 'uma ladra experiente', 'uma feiticeira do vento', 'um mentor invisível', 'uma anciã do clã', 
'um guardião da floresta', 'uma barda viajante', 'um cavaleiro fantasma', 'uma sacerdotisa do sol', 'um mestre da guerra', 'uma maga da noite', 'um ancião do deserto', 'uma ladra das sombras', 'um guerreiro da tempestade', 'uma druida lunar', 'um feiticeiro das estrelas', 'uma guardiã antiga', 
'um professor de magia', 'uma feiticeira errante', 'um caçador de tesouros', 'uma guardiã da floresta', 'um guerreiro silencioso', 'uma druida sábia', 'um bardo da luz', 'uma sacerdotisa da terra', 'um mestre do gelo', 'uma feiticeira do fogo', 'um caçador de sombras', 'uma anciã guardiã do clã', 'um guerreiro de honra', 'uma aprendiz de maga', 'um mestre alquimista lendário', 'uma guardiã da floresta ancestral']

# Lista para eventos do personagem
eventos = ['perdeu tudo em um ataque de bandidos', 'descobriu poderes mágicos', 'foi exilado injustamente', 'sobreviveu a um naufrágio', 'encontrou um artefato antigo', 'salvou um amigo em perigo', 'foi traído por aliados', 'sobreviveu a uma emboscada', 'foi capturado e aprisionado', 
'descobriu uma profecia sobre si mesmo', 'derrotou um monstro temido', 'participou de uma guerra civil', 'escapou de uma masmorra infernal', 'recebeu uma maldição', 'domou uma criatura selvagem', 'descobriu um segredo de família', 'sobreviveu a uma doença mortal', 'foi mentor de um jovem prodígio', 
'participou de um torneio lendário', 'desvendou um mistério antigo', 'perdeu sua terra natal', 'foi adotado por estrangeiros', 'sobreviveu a um desastre natural', 'aprendeu a magia proibida', 'desafiou um tirano', 'descobriu uma caverna secreta', 'recebeu uma bênção divina', 
'enfrentou um espírito vingativo', 'escapou de um culto maligno', 'foi amaldiçoado por uma bruxa', 'descobriu sua verdadeira linhagem', 'sobreviveu a um ataque de dragões', 'aprendeu artes marciais secretas', 'encontrou um antigo grimório', 'foi aprisionado por um rei injusto', 
'sobreviveu a um colapso de mina', 'descobriu uma passagem secreta', 'foi perseguido por um assassino', 'salvou uma criatura mágica','descobriu habilidades psíquicas', 'foi testado por um deus', 'participou de uma revolução', 'encontrou um tesouro perdido', 'aprendeu a linguagem dos animais', 
'foi enganado por um aliado', 'enfrentou uma invasão de goblins', 'recebeu treinamento secreto', 'descobriu uma relíquia perdida', 'foi aceito em uma ordem secreta', 'sobreviveu a uma avalanche', 'aprendeu a arte da furtividade', 'descobriu um mundo paralelo', 
'foi amaldiçoado por um espírito antigo', 'sobreviveu a uma batalha naval', 'encontrou um mentor misterioso', 'aprendeu a manipular elementos', 'sobreviveu a um ataque de trolls', 'foi enganado por um mercador', 'descobriu um templo antigo', 'recebeu instruções de um espírito guardião', 
'enfrentou monstros lendários', 'descobriu uma caverna de cristais', 'sobreviveu a um terremoto', 'foi treinado por um mestre ancião', 'aprendeu magia elemental', 'descobriu segredos de alquimia', 'enfrentou um exército inimigo', 'sobreviveu a um ataque de piratas', 'aprendeu a arte da diplomacia', 
'descobriu um mapa perdido', 'foi aceito em uma guilda de aventureiros', 'sobreviveu a um incêndio', 'encontrou um aliado inesperado', 'aprendeu técnicas de camuflagem', 'foi amaldiçoado por um monstro', 'descobriu um artefato lendário', 'sobreviveu a um ataque de orcs', 
'aprendeu a linguagem das runas', 'enfrentou um espírito vingativo', 'foi guiado por uma entidade misteriosa', 'descobriu uma biblioteca secreta', 'participou de uma expedição perigosa', 'sobreviveu a um desastre mágico', 'foi traído por um amigo', 'descobriu segredos ancestrais', 
'aprendeu a manipular sombras', 'sobreviveu a um ataque de lobos', 'foi escolhido por um espírito guardião', 'descobriu uma habilidade oculta', 'sobreviveu a uma invasão de mortos-vivos', 'enfrentou um dragão antigo', 'foi exilado de sua terra natal', 'descobriu um poder ancestral', 'sobreviveu a uma tempestade mortal']

# Habilidades especiais
habilidade = ['aprendeu a manejar a espada', 'dominou magia elemental', 'se tornou ágil como um ladrão', 'aprendeu técnicas de sobrevivência', 'desenvolveu grande inteligência estratégica', 'aprendeu a cura por ervas', 'desenvolveu reflexos sobre-humanos', 'aprendeu a atirar com arco', 
'dominou artes marciais', 'aprendeu a manipular sombras', 'desenvolveu grande resistência física', 'aprendeu línguas antigas', 'dominou encantamentos', 'aprendeu a arte da diplomacia', 'desenvolveu habilidades de camuflagem', 'aprendeu a controlar elementos', 'domou um animal feroz', 
'aprendeu a abrir fechaduras', 'dominou técnicas de furtividade', 'aprendeu a criar poções', 'aprendeu a invocar criaturas', 'dominou combate com duas armas', 'aprendeu a controlar o vento', 'desenvolveu sentidos aguçados', 'aprendeu a manipular fogo', 'aprendeu a manipular água', 
'aprendeu a manipular terra', 'aprendeu a manipular gelo', 'aprendeu a manipular relâmpago', 'aprendeu técnicas de alquimia', 'aprendeu a manipular ilusões', 'aprendeu a curar ferimentos graves', 'dominou combate corpo a corpo', 'aprendeu técnicas de espionagem', 'aprendeu a rastrear inimigos', 
'desenvolveu força sobre-humana', 'aprendeu a se comunicar com animais', 'aprendeu a criar armadilhas', 'aprendeu a forjar armas', 'aprendeu a criar poções mágicas', 'aprendeu a invocar espíritos', 'aprendeu a se camuflar na natureza', 'dominou magia de proteção', 'aprendeu a manipular metais', 
'aprendeu a manipular madeira', 'aprendeu a manipular venenos', 'aprendeu a controlar a mente', 'aprendeu a manipular energia vital', 'dominou técnicas de arquearia avançada', 'aprendeu a se mover silenciosamente', 'aprendeu a decifrar runas antigas', 'aprendeu a controlar sombras', 
'aprendeu técnicas de combate com bastão', 'aprendeu a manipular gravidade', 'aprendeu a detectar mentiras', 'aprendeu a manipular tempo em pequena escala', 'aprendeu técnicas de combate com lanças', 'aprendeu a manipular luz', 'aprendeu a criar portais', 'aprendeu a controlar plantas', 
'aprendeu a detectar magia', 'aprendeu a invocar elementais', 'aprendeu a manipular pedras preciosas', 'aprendeu a sobreviver em ambientes extremos', 'aprendeu técnicas de natação avançada', 'aprendeu a escalar qualquer superfície', 'aprendeu a criar bombas mágicas', 'aprendeu a controlar fogo sagrado', 
'aprendeu a usar arcos mágicos', 'aprendeu a manipular energia espiritual', 'aprendeu a conjurar ilusões realistas', 'aprendeu a curar doenças', 'aprendeu a se teletransportar pequenas distâncias', 'aprendeu a criar encantamentos para armas', 'aprendeu técnicas de luta com escudo', 'aprendeu a controlar criaturas menores', 'aprendeu a manipular gelo avançado', 'aprendeu a detectar inimigos ocultos', 
'aprendeu a manipular água avançada', 'aprendeu a manipular vento avançado', 'aprendeu a criar armaduras mágicas', 'aprendeu a conjurar luz sagrada', 'aprendeu a manipular sombras avançadas', 'aprendeu a manipular energia do caos', 'aprendeu a controlar animais selvagens', 
'aprendeu a usar feitiços de proteção', 'aprendeu a detectar armadilhas', 'aprendeu a manipular eletricidade', 'aprendeu a conjurar tempestades pequenas', 'aprendeu a manipular magma', 'aprendeu técnicas de combate com espadas duplas', 'aprendeu a controlar criaturas fantasmagóricas', 
'aprendeu a criar poções de invisibilidade', 'aprendeu a controlar a mente de animais', 'aprendeu a conjurar barreiras mágicas', 'aprendeu a manipular vento e tempestade', 'aprendeu a invocar espíritos guardiões', 'aprendeu a controlar chamas negras', 'aprendeu técnicas de combate com maça', 'aprendeu a manipular cristais', 'aprendeu a criar feitiços de ilusão avançados']