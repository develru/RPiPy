class GPIOrtx(object):

    def __init__(self, io=4):
            self._gpioNum = io

    def exportGPIO(self):
        try:
            gpioFileExport = open("/sys/class/gpio/export")
        except IOError:
            print("OPERATION FAILED: Unable to export GPIO{}!".format(
                self._gpioNum))

        gpioFileExport.write = self._gpioNum
        gpioFileExport.close        