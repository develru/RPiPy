class GPIOrtx(object):

    def __init__(self, io='4'):
            self._gpioNum = io

    def export(self):
        try:
            gpioFileExport = open('/sys/class/gpio/export', 'w')
            gpioFileExport.write(self._gpioNum)
            gpioFileExport.close
        except IOError:
            print('OPERATION FAILED: Unable to export GPIO{}!'.format(
                self._gpioNum))

    def unexport(self):
        try:
            gpioFileUnexport= open('/sys/class/gpio/unexport', 'w')
            gpioFileUnexport.write(self._gpioNum)
            gpioFileUnexport.close
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
