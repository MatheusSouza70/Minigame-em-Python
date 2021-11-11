import time 

#Procurando brechas sobre como os usuários podem responder as perguntas.
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["S", "s", "sim"]
no = ["N", "n", "nao", "não"]

#Objetos
espada = 0
flor = 0

required = ("\nUse apenas A, B, or C\n") #aviso ao usuário sobre o limite de respostas

#A história é feita em seções, começando com a intro.
def intro():
  print("Você é um plebeu e, em um dia, decide sair com seus amigos. Vocês vão na taverna “O Bode Dourado”, na cidade de Odin. Esta cidade é um movimentado entreposto comercial a meio caminho de todas as principais rotas mercantis entre os reinos do leste")
  time.sleep(1)
  print ("")
  time.sleep(1)
  print ("Depois de uma noite de bebedeira com amigos, você acorda na manhã seguinte em uma floresta densa e úmida. " 
  "Cabeça girando e lutando contra a vontade de vomitar, você se levanta e se maravilha com o seu novo ambiente desconhecido. "
  "A paz desaparece rapidamente quando você ouve um som grotesco emitido atrás de você. Um Orc babando está correndo em sua direção. Você irá:")
  time.sleep(1)
  print (" A. Pegue uma pedra próxima e jogue-a no Orc |"
  " B. Deite-se e espere ser atacado. |"
  " C. Correr!")
  choice = input(">>> ") #Primeira escolha
  if choice in answer_A:
    option_pedra()
  elif choice in answer_B:
    time.sleep(1)
    print ("\n É, essa foi rápida..."
    "\n\nVocê morreu!")
  elif choice in answer_C:
    option_correr()
  else:
    print (required)
    intro()

def option_pedra(): 
  print ("\nO Orc fica atordoado, mas recupera o controle. Ele começa correndo em sua direção novamente. Você vai: ")
  time.sleep(1)
  print ("  A. Correr novamente |"
  " B. Jogar outra pedra |"
  " C. Correr para uma caverna próxima")
  choice = input(">>> ")
  if choice in answer_A:
    option_correr()
  elif choice in answer_B:
    print ("\n Você decide jogar outra pedra. " 
    " A primeira pedra não deu muito dano. A pedra ricocheteou na cabeça e você erra. \n\n Você morreu! ")
  elif choice in answer_C:
    option_caverna()
  else:
    print (required)
    option_pedra()

def option_caverna():
  print ("\nVocê estava hesitante, já que a caverna estava escura e sinistra. "
    " Antes de entrar totalmente, você nota você nota um báu parcialmente enterrado no chão. "
    " Ao abrir, você encontra uma espada cintilante. Deseja pega-lá? Sim / Não? ")
  choice = input(">>> ")
  if choice in yes:
    espada = 1 #Adiciona a espada em seu inventário
  else:
    espada = 0
  print ("\n O Orc continua a te perseguir, você está em apuros. O que fará em seguida? ")
  time.sleep(1)
  print ("  A. Se esconder em silêncio |"
  " B. Lutar |"
  " C. Correr")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nMesmo? Você vai se esconder no escuro? Eu penso que "
    "Orcs podem ver muito bem no escuro, certo? Não tenho certeza, mas "
    "Vou com SIM, então ... \n\n Você morreu! ")
  elif choice in answer_B:
   if espada > 0:
    print ("\nVocê ficou esperando. A espada cintilante atraiu "
    "o Orc, que pensou que você não era páreo. Enquanto ele caminhava "
    "cada vez mais perto, seu coração bate mais rápido. Como o Orc "
    "estendeu a mão para agarrar a espada, você perfurou a lâmina em "
    "seu peito. \n \n Você sobreviveu! ")
   else: #Se o usuario não pegar a espada...
     print ("\n Você deveria ter pegado aquela espada. Você está indefeso. \n\n Você morreu! ")
  elif choice in answer_C:
    print ("Quando o Orc entra na caverna escura, você ligeiramente "
    "foge. Você está a vários metros de distância, mas o Orc olha "
    "ao redor e vê você correndo. ")
    option_correr()
  else:
    print (required)
    option_caverna()

def option_correr():
  print ("\nVocê corre o mais rápido possível, mas a "
  "a velocidade do Orc é muito grande. Você irá: ")
  time.sleep(1)
  print ("  A. Esconder-se atrás da rocha |"
  " B. Fazer uma armadilha, e então lutar |"
  " C. Corra em direção a uma cidade abandonada |")
  choice = input(">>> ")
  if choice in answer_A:
    print ("Você é facilmente visto "
    "\n\nVocê morreu!")
  elif choice in answer_B:
    print ("\nVocê não é páreo para um Orc. "
    "\n\nVocê morreu!")
  elif choice in answer_C:
    option_cidade()
  else:
    print (required)
    option_correr()
    
def option_cidade():
  print ("\nEnquanto corre freneticamente, você percebe uma espada enferrujada "
  "caída na lama. Você rapidamente se abaixa e a pega, "
  "mas erra. Você tenta acalmar sua respiração pesada enquanto se esconde "
  "atrás de um edifício delapitado, esperando o Orc chegar "
  "correndo na esquina. Você nota uma flor roxa "
  "perto do seu pé. Você a pega? Sim / Não?")
  choice = input(">>> ")
  if choice in yes:
    flor = 1 #adiciona a flor
  else:
    flor = 0
  print ("Você ouve seus passos pesados ​​e se prepara para "
  "o Orc iminente.")
  time.sleep(1)
  if flor > 0:
    print ("\nVocê rapidamente pega a flor roxa, de alguma forma "
    "esperando que isso pare o Orc. Pare! O Orc estava apenas procurando "
    "por amor. "
    "\n\nIsso foi bem estranho... Mas você sobreviveu! ")
  else: #If the user didn't grab the espada
     print ("\nTalvez você devesse ter pego a flor... "
     "\n\nVocê morre esmagado pelo Orc. ")

intro()