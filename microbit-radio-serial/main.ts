radio.setTransmitPower(7)
radio.setGroup(235)

basic.forever(() => {
    let l = serial.readLine()
    //serial.writeLine("E:" + l)
    radio.sendString(l)
})

radio.onDataReceived(() => {
    let v = radio.receiveString()
    serial.writeLine(v)
})
