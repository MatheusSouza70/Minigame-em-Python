import time
import PySimpleGUI as sg

# Procurando brechas sobre como os usuários podem responder as perguntas.
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["S", "s", "sim"]
no = ["N", "n", "nao", "não"]

# Objetos
espada = 0
flor = 0

# aviso ao usuário sobre o limite de respostas
required = ("\nUse apenas A, B, or C\n")

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
    return sg.Window("A história começa", layout=layout, finalize=True, )

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


def janela_choicePedra():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nO Orc fica atordoado, mas recupera o controle.\nEle começa a correr em sua direção novamente. Você vai: ")],
        [sg.Text('Correr'), sg.Button('A')],
        [sg.Text('Jogar outra pedra'), sg.Button('B')],
        [sg.Text('Correr para uma caverna próxima'), sg.Button('C')]
    ]
    return sg.Window("Uma pedra ??", layout=layout, finalize=True)


def janela_choiceDeitar():
    sg.theme("Reddit")
    layout = [
        [sg.Text('Essa foi rápida...\nVocê morreu')],
        [sg.Text('')],
        [sg.Button('Recomeçar??'), sg.Button('Sair..')]
    ]
    return sg.Window("Rápido como o vento", layout=layout, finalize=True, size=(300, 100))


def janela_choiceCorrer():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nVocê corre o mais rápido possível,\nmas a "
                 "a velocidade do Orc é muito grande. Você irá: ")],
        [sg.Text('Esconder-se atrás da rocha '), sg.Button('A')],
        [sg.Text('Fazer uma armadilha, e então lutar'), sg.Button('B')],
        [sg.Text('Corra em direção a um cidade abandonada'), sg.Button('C')]
    ]
    return sg.Window("The Flash ?", layout=layout, finalize=True)


def janela_choicePedraF():
    sg.theme("Reddit")
    layout = [
        [sg.Text("\nVocê decide jogar outra pedra. "
                 " A primeira pedra não deu muito dano.\nA pedra ricocheteou na cabeça e você erra. \nVocê morreu! ")],
        [sg.Text('')],
        [sg.Button('Recomeçar??'), sg.Button('Sair..')]

    ]
    return sg.Window("Não foi dessa vez", layout=layout, finalize=True)


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


def janela_choiceEspada():
    sg.theme("Reddit")
    layout = [
        []
    ]


janela1, janela2 = janela_inicial(), None
janela3 = None
janela4 = None
janela5 = None

while True:
    window, event, values = sg.read_all_windows()
    # Escolha página inicial
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'sair':
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
        janela4 = janela_choiceCorrer
        janela3.hide()
    if window == janela3 and event == 'B':
        janela4 = janela_choicePedraF()
        janela3.hide()
    if window == janela3 and event == 'C':
        janela4 = janela_choiceCaverna

    # choice pedraF
    if window == janela4 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == ('Recomeçar??'):
        janela1 = janela_inicial()
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
        if values['resposta'] == yes:
            janela5 = janela_choiceEspada()
            janela4.hide()
            espada = 1
        if values['resposta'] == no:
            janela5 = janela_choiceEspada()
            janela4.hide()
            espada = 0

# Faltando choice A depois da escolha A
