# importando a biblioteca PySimpleGUI para a interface
import PySimpleGUI as sg

# Procurando brechas sobre como os usuários podem responder as perguntas.
yes = ["S", "s", "sim"]
no = ["N", "n", "nao", "não"]

# Objetos
espada = 0
flor = 0

# Primeira janela


def janela_inicial():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Seja bem vindo!')],
        [sg.Text('')],
        [sg.Text('Você está a entrar em uma aventura.')],
        [sg.Text('')],
        [sg.Text('Clique em ok para continuar')],
        [sg.Button('Sair'), sg.Button('Ok')]
    ]
    return sg.Window("Vamos ??", layout=layout, finalize=True, size=(300, 180))

# segunda janela


def janela_comeco():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Você é um plebeu e, em um dia, decide sair com seus amigos.\nVocês vão na taverna “O Bode Dourado”, na cidade de Odin.\nEsta cidade é um movimentado entreposto comercial a\nmeio caminho de todas as principais rotas mercantis\nentre os reinos do leste")],
        [sg.Text('...')],
        [sg.Text("Depois de uma noite de bebedeira com amigos,\nvocê acorda na manhã seguinte\nem uma floresta densa e úmida. "
                 "\nCabeça girando e lutando contra a vontade de vomitar,\nvocê se levanta e se maravilha com o seu novo ambiente desconhecido. "
                 "\nA paz desaparece rapidamente quando você ouve um som grotesco \nemitido atrás de você.\nUm Orc babando está correndo em sua direção. Você irá:")],
        [sg.Text("Pegue uma pedra próxima e jogue-a no Orc "), sg.Button('A')],
        [sg.Text("Deite-se e espere ser atacado. "), sg.Button('B')],
        [sg.Text("Correr! "), sg.Button('C')]
    ]
    return sg.Window("A história começa", layout=layout, finalize=True, size=(450, 400))

# escolha jogar pedra


def janela_choicePedra():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nO Orc fica atordoado, mas recupera o controle.\nEle começa a correr em sua direção novamente. Você vai: ")],
        [sg.Text('Correr'), sg.Button('A')],
        [sg.Text('Jogar outra pedra'), sg.Button('B')],
        [sg.Text('Correr para uma caverna próxima'), sg.Button('C')]
    ]
    return sg.Window("Uma pedra ??", layout=layout, finalize=True)

# escolha deitar e esperar ser atacado


def janela_choiceDeitar():
    sg.theme("Reddit")
    layout = [
        [sg.Text('Essa foi rápida...\nVocê morreu')],
        [sg.Text('')],
        [sg.Button('Recomeçar??'), sg.Button('Sair..')]
    ]
    return sg.Window("Rápido como o vento", layout=layout, finalize=True, size=(300, 100))

# escolha correr


def janela_choiceCorrer():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nVocê corre o mais rápido possível,\nmas a "
                 "a velocidade do Orc é muito grande. Você irá: ")],
        [sg.Text('Esconder-se atrás da rocha '), sg.Button('A')],
        [sg.Text('Fazer uma armadilha, e então lutar'), sg.Button('B')],
        [sg.Text('Corra em direção a um cidade'), sg.Button('C')]
    ]
    return sg.Window("The Flash ?", layout=layout, finalize=True)

# esxolha de jogar a pedra e acabar morrendo


def janela_choicePedraF():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nVocê decide jogar outra pedra. "
                 " A primeira pedra não deu muito dano.\nA pedra ricocheteou na cabeça e você erra. \nVocê morreu! ")],
        [sg.Text('')],
        [sg.Button('Recomeçar??'), sg.Button('Sair..')]

    ]
    return sg.Window("Não foi dessa vez", layout=layout, finalize=True)

# escolha da caverna


def janela_choiceCaverna():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nVocê estava hesitante, já que a caverna estava escura e sinistra. "
                 " \nAntes de entrar totalmente, você nota você nota um báu parcialmente enterrado no chão. "
                 " \nAo abrir, você encontra uma espada cintilante. Deseja pega-lá? Sim / Não? ")],
        [sg.Text('')],
        [sg.Input(key='resposta')],
        [sg.Button('Ok')]
    ]
    return sg.Window("A caverna pegar ou largar ", layout=layout, finalize=True)

# escolha depois de pegar a espada


def janela_choiceEspada():
    sg.theme("Reddit")
    layout = [
        [sg.Text(
            "\n O Orc continua a te perseguir, você está em apuros. O que fará em seguida? ")],
        [sg.Text('Se esconder em silêncio'), sg.Button('A')],
        [sg.Text('Lutar'), sg.Button('B')],
        [sg.Text('Correr'), sg.Button('C')]
    ]
    return sg.Window("E agora ??", layout=layout, finalize=True)

# escolha de lutar após pegar a espada


def janela_choiceEspada1():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nVocê ficou esperando. A espada cintilante atraiu "
                 "o Orc,\nque pensou que você não era páreo.\nEnquanto ele caminhava "
                 "cada vez mais perto,\nseu coração bate mais rápido. Como o Orc "
                 "estendeu a mão para agarrar a espada,\nvocê perfurou a lâmina em "
                 "seu peito. \n \n Você sobreviveu! ")],
        [sg.Button('Recomeçar??'), sg.Button('Sair..')]
    ]
    return sg.Window("Grande Final", layout=layout, finalize=True)

# escolha de lutar sem ter pego a espada


def janela_choiceEspada0():
    sg.theme("Reddit")
    layout = [
        [sg.Text(
            "\n Você deveria ter pegado aquela espada.\nVocê está indefeso. \n Você morreu! ")],
        [sg.Button('Recomeçar??'), sg.Button('Sair..')]
    ]
    return sg.Window("Por uma espada..", layout=layout, finalize=True)

# escolha de ficar no escuro


def janela_choiceEscuro():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nMesmo? Você vai se esconder no escuro?\nEu penso que "
                 "Orcs podem ver muito bem no escuro, certo?\nNão tenho certeza, mas "
                 "Vou com SIM, então ... \n Você morreu! ")],
        [sg.Button('Recomeçar??'), sg.Button('Sair..')]
    ]

# escolha de se esconder atrás da rocha


def janela_choiceRocha():
    sg.theme("Reddit")
    layout = [
        [sg.Text('Você foi facilmente visto')],
        [sg.Text('Você morreu!')],
        [sg.Button('Recomeçar??'), sg.Button('Sair..')]
    ]
    return sg.Window("Não foi dessa vez", layout=layout, finalize=True, size=(270, 100))

# escolha de fazer armadilha


def janela_choiceArmadilha():
    sg.theme("Reddit")
    layout = [
        [sg.Text('Você não é pareo para o orc')],
        [sg.Text('Você morreu')],
        [sg.Button('Recomeçar??'), sg.Button('Sair..')]
    ]
    return sg.Window("Não foi dessa vez", layout=layout, finalize=True, size=(270, 100))

# escolha de ir para cidade


def janela_choiceCidade():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nEnquanto corre freneticamente, você percebe uma espada enferrujada "
                 "caída na lama. Você rapidamente se abaixa e a pega,\n"
                 "\nmas erra. Você tenta acalmar sua respiração pesada enquanto se esconde "
                 "\natrás de um edifício delapitado, esperando o Orc chegar "
                 "\ncorrendo na esquina. Você nota uma flor roxa "
                 "\nperto do seu pé. Você a pega? Sim / Não?")],
        [sg.Input(key='resposta')],
        [sg.Button('Ok')]
    ]
    return sg.Window("A cidade", layout=layout, finalize=True)

# escolha de pegar a flor


def janela_choiceFlor1():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nVocê rapidamente pega a flor roxa, de alguma forma "
                 "\nesperando que isso pare o Orc. Pare! \nO Orc estava apenas procurando "
                 "por amor. "
                 "\nIsso foi bem estranho... Mas você sobreviveu! ")],
        [sg.Button('Recomeçar??'), sg.Button('Sair..')]

    ]
    return sg.Window("You win!!", layout=layout, finalize=True)

# escolha de não pegar a flor


def janela_choiceFlor0():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nTalvez você devesse ter pego a flor... "
                 "\nVocê morre esmagado pelo Orc. ")],
        [sg.Button('Recomeçar??'), sg.Button('Sair..')]
    ]
    return sg.Window("You lose..", layout=layout, finalize=True)


# definindo o valor das variaveis
janela1, janela2 = janela_inicial(), None
janela3 = None
janela4 = None
janela5 = None
janela6 = None
# utilizando listas para definir o valor das variaveis
yes = ["S", "s", "sim", "Sim"]
no = ["N", "n", "nao", "não"]

# estrutura de repetição
while True:
    # definindo para as variaveis serem lidas em todas as janelas / verificando condições e escolhas
    window, event, values = sg.read_all_windows()
    # Escolha página inicial
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Sair':
        break
    if window == janela1 and event == 'Ok':
        janela2 = janela_comeco()
        janela1.hide()

    # inicio da história / segunda janela
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == 'A':
        janela3 = janela_choicePedra()
        janela2.hide()
    if window == janela2 and event == 'B':
        janela3 = janela_choiceDeitar()
        janela2.hide()
    if window == janela2 and event == 'C':
        janela3 = janela_choiceCorrer()
        janela2.hide()

    # janela choice A
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == 'A':
        janela4 = janela_choiceRocha()
        janela3.hide()
    if window == janela3 and event == 'B':
        janela4 = janela_choicePedraF()
        janela3.hide()
    if window == janela3 and event == 'C':
        janela4 = janela_choiceCidade()
        janela3.hide()

    # janela 4
    if window == janela4 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == 'A':
        janela5 = janela_choiceRocha()
        janela4.hide()
    if window == janela4 and event == 'B':
        janela5 = janela_choiceArmadilha()
        janela4.hide()
    if window == janela4 and event == 'C':
        janela5 = janela_choiceCidade()
        janela4.hide()

    # morte choice rocha
    if window == janela5 and event == sg.WIN_CLOSED:
        break
    if window == janela5 and event == ('Recomeçar??'):
        janela1 = janela_inicial()
        janela5.hide()
    if window == janela5 and event == ('Sair..'):
        break

    # choice cidade
    if window == janela5 and event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        if window == janela5 and values['resposta'] == yes[0]:
            janela6 = janela_choiceFlor1()
            janela5.hide()
            flor = 1  # adiciona a flor a seu inventario
        if window == janela5 and values['resposta'] == yes[1]:
            janela6 = janela_choiceFlor1()
            janela5.hide()
            flor = 1
        if window == janela5 and values['resposta'] == yes[2]:
            janela6 = janela_choiceFlor1()
            janela5.hide()
            flor = 1
        if window == janela5 and values['resposta'] == yes[3]:
            janela6 = janela_choiceFlor1()
            janela5.hide()
            flor = 1
        if window == janela5 and values['resposta'] == no[0]:
            flor = 0
            janela6 = janela_choiceFlor0()
            janela5.hide()
        if window == janela5 and values['resposta'] == no[1]:
            flor = 0
            janela6 = janela_choiceFlor0()
            janela5.hide()
        if window == janela5 and values['resposta'] == no[2]:
            flor = 0
            janela6 = janela_choiceFlor0()
            janela5.hide()
        if window == janela5 and values['resposta'] == no[3]:
            flor = 0
            janela6 = janela_choiceFlor0()
            janela5.hide()

    # cidade win
    if window == janela6 and event == sg.WIN_CLOSED:
        break
    if window == janela6 and event == ('Recomeçar??'):
        janela1 = janela_inicial()
        janela6.hide()
    if window == janela6 and event == ('Sair..'):
        break

    # choice pedraF
    if window == janela4 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == ('Recomeçar??'):
        janela1 = janela_inicial()
        janela4.hide()
    if window == janela4 and event == ('Sair..'):
        break

    # janela choice B / morte / reiniciar
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == 'Recomeçar??':
        janela1 = janela_inicial()
        janela3.hide()
    if window == janela3 and event == 'Sair..':
        break

    # janela choice Caverna
    if window == janela4 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == 'Ok':
        if values['resposta'] == yes[0]:
            janela5 = janela_choiceEspada()
            janela4.hide()
            espada = 1
        if values['resposta'] == yes[1]:
            janela5 = janela_choiceEspada()
            janela4.hide()
            espada = 1
        if values['resposta'] == yes[2]:
            janela5 = janela_choiceEspada()
            janela4.hide()
            espada = 1
        if values['resposta'] == yes[3]:
            janela5 = janela_choiceEspada()
            janela4.hide()
            espada = 1
        if values['resposta'] == no[0]:
            janela5 = janela_choiceEspada()
            janela4.hide()
            espada = 0
        if values['resposta'] == no[1]:
            janela5 = janela_choiceEspada()
            janela4.hide()
            espada = 0
        if values['resposta'] == no[2]:
            janela5 = janela_choiceEspada()
            janela4.hide()
            espada = 0
        if values['resposta'] == no[3]:
            janela5 = janela_choiceEspada()
            janela4.hide()
            espada = 0
    # janela de escolha dentro da caverna
    if window == janela5 and event == sg.WIN_CLOSED:
        break
    if window == janela5 and event == 'A':
        janela6 = janela_choiceEscuro()
        janela5.hide()
    if window == janela5 and event == 'B':
        if espada > 0:
            janela6 = janela_choiceEspada1()
            janela5.hide()
        else:
            janela6 = janela_choiceEspada0()
            janela5.hide()
    if window == janela5 and event == 'C':
        janela3 = janela_choiceCorrer()
        janela5.hide()
    # janela final
    if window == janela6 and event == sg.WIN_CLOSED:
        break
    if window == janela6 and event == 'Recomeçar??':
        janela1 = janela_inicial()
        janela6.hide()
    if window == janela6 and event == 'Sair..':
        break
