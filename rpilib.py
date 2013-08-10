class GPIOrtx(object):

    def __init__(self, io='4'):
            self._gpioNum = io
            self._state = 0

    def export(self):
        try:
            gpioFileExport = open('/sys/class/gpio/export', 'w')
            gpioFileExport.write(self._gpioNum)
            gpioFileExport.close
            self._state = 1
        except IOError:
            print('OPERATION FAILED: Unable to export GPIO{}!'.format(
                self._gpioNum))

    def unexport(self):
        try:
            gpioFileUnexport = open('/sys/class/gpio/unexport', 'w')
            gpioFileUnexport.write(self._gpioNum)
            gpioFileUnexport.close
            self._state = 0
        except IOError:
            print('OPERATION FAILED: Unable to unexport GPIO{}!'.format(
                self._gpioNum))

    def setDirection(self, direction):
        try:
            gpioFile = open('/sys/class/gpio/gpio' + self._gpioNum +
                            '/direction', 'w')
            gpioFile.write(direction)
            gpioFile.close()
        except IOError:
            print(
                'OPERATION FAILED: Unable to set direction for GPIO{}!'.format(
                    self._gpioNum))

    def writeValue(self, value):
        try:
            gpioFile = open('/sys/class/gpio/gpio' + self._gpioNum + '/value',
                            'w')
            gpioFile.write(value)
            gpioFile.close
        except IOError:
            print('OPERATION FAILED: Unable to write value to GPIO{}!'.format(
                self._gpioNum))

    def setup(self, direction):
        self.export()
        self.setDirection(direction)


class LCD16x2(object):
    # commands
    LCD_CLEARDISPLAY = 0x01
    LCD_RETURNHOME = 0x02
    LCD_ENTRYMODESET = 0x04
    LCD_DISPLAYCONTROL = 0x08
    LCD_CURSORSHIFT = 0x10
    LCD_FUNCTIONSET = 0x20
    LCD_SETCGRAMADDR = 0x40
    LCD_SETDDRAMADDR = 0x80

    # flags for display entry mode
    LCD_ENTRYRIGHT = 0x00
    LCD_ENTRYLEFT = 0x02
    LCD_ENTRYSHIFTINCREMENT = 0x01
    LCD_ENTRYSHIFTDECREMENT = 0x00

    # flags for display
    # on/off control
    LCD_DISPLAYON = 0x04
    LCD_DISPLAYOFF = 0x00
    LCD_CURSORON = 0x02
    LCD_CURSOROFF = 0x00
    LCD_BLINKON = 0x01
    LCD_BLINKOFF = 0x00

    # flags
    # for
    # display/cursor
    # shift
    LCD_DISPLAYMOVE = 0x08
    LCD_CURSORMOVE = 0x00

    # flags
    # for
    # display/cursor
    # shift
    LCD_DISPLAYMOVE = 0x08
    LCD_CURSORMOVE = 0x00
    LCD_MOVERIGHT = 0x04
    LCD_MOVELEFT = 0x00

    # flags
    # for
    # function
    # set
    LCD_8BITMODE = 0x10
    LCD_4BITMODE = 0x00
    LCD_2LINE = 0x08
    LCD_1LINE = 0x00
    LCD_5x10DOTS = 0x04
    LCD_5x8DOTS = 0x00
