import pyautogui as pg
num = int(input("Antes de prosseguir, insira o numero de contatos que serão enviados as mensagens: "))

wait = 1.5
count = 1
pg.alert('INICIANDO CÓDIGO, NAO USE O COMPUTADOR.\n\tCopie a mensagem que deverá ser enviada e o codigo irá colar e enviar para os contatos.\n\tAbra o WhatsApp Web,clique na primeira conversa e, em seguida, aperte o botão "OK" abaixo.\n')
pg.PAUSE = 0.5

for i in range(0, num):
    pg.click(x=804, y=736)
    for j in range(0, i):
        pg.hotkey("ctrlleft", "shiftleft", "altleft", "]")
    pg.hotkey('ctrlleft', 'v')
    pg.press("enter")
