_1 = False

def on_button_pressed_a():
    global _1
    _1 = False
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    global _1
    _1 = True
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_b():
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if _1:
        if input.light_level() < 50:
            basic.show_icon(IconNames.HEART)
            basic.clear_screen()
basic.forever(on_forever)
