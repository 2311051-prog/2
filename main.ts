let _1 = false
input.onButtonPressed(Button.A, function () {
    _1 = false
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    _1 = true
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
})
basic.forever(function () {
    if (_1) {
        if (input.lightLevel() < 50) {
            basic.showIcon(IconNames.Heart)
            basic.clearScreen()
        }
    }
})
