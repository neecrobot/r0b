POSITION = 0
X = 0
Y = 0
START = 0
basic.show_icon(IconNames.HEART)

def on_forever():
    global X, Y, POSITION, START
    while START == 1:
        for カウンター in range(16):
            led.plot(X, Y)
            basic.pause(100)
            led.unplot(X, Y)
            if カウンター < 4:
                X += 1
            elif カウンター < 8:
                Y += 1
            elif カウンター < 12:
                X += -1
            else:
                Y += -1
            if input.button_is_pressed(Button.B):
                POSITION = カウンター
                START = 2
            break
basic.forever(on_forever)

def on_forever2():
    global POSITION
    if input.button_is_pressed(Button.A):
        POSITION = 1
basic.forever(on_forever2)
