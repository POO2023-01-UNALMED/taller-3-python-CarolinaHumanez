class Control:

    def __init__(self,tv):
        self._tv=tv

    def turnOff(self):
        self._tv.turnOff()

    def turnOn(self):
        self._tv.turnOn()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self,canal):
        self._tv.setCanal(canal)

    def enlazar(self,tv):
        self._tv=tv
        tv.control=self

    def setTv(self,newTv):
        self._tv=newTv

    def getTv(self):
        return self._tv