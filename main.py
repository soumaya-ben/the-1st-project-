number = 0

def on_button_pressed_a():
    global number
    number = 0
    if True:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_number(0)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
