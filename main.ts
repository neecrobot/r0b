let X = 0
let Y = 0
basic.forever(function () {
    for (let COUNT = 0; COUNT <= 15; COUNT++) {
        led.unplot(X, Y)
        if (COUNT < 4) {
            X = COUNT
            Y = 0
        } else if (COUNT < 8) {
            X = 4
            Y = COUNT - 4
        } else if (COUNT < 12) {
            X = 12 - COUNT
            Y = 4
        } else {
            X = 0
            Y = 16 - COUNT
        }
        led.plot(X, Y)
        basic.pause(100)
    }
})
