
class Marca:

    def __init__(self,nombre):
        self._nombre=nombre

    def setNombre(self,nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

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

class TV:
    numTv=0
    def __init__(self,marca,estado):
        self._marca=marca
        self._estado=estado
        self.canal=1
        self.precio=500
        self.volumen=1
        self.control=None

    def getMarca(self):
        return self._marca.getNombre()
    def setMarca(self,marca):
        self._marca=marca

    def getControl(self):
        return self.control
    def setControl(self,control):
        self.control=control

    def getPrecio(self):
        return self.precio
    def setPrecio(self,precio):
        self.precio=precio

    def getVolumen(self):
        return self.volumen
    def setVolumen(self,volumen):
        if (self._estado==True):
            if(volumen>=0 and volumen<=7):
                self.volumen=volumen

    def getCanal(self):
        return self.canal
    def setCanal(self,canal):
        if(self._estado==True):
            if(canal>=1 and canal<=120):
                self.canal=canal

    def getNumTv(self):
        return numTV

    def getEstado(self):
        return self._estado
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False

    def canalUp(self):
        if (self._estado==True):
            if (self.canal<120):
                self.canal+=1

    def canalDown(self):
        if (self._estado==True):
            if (self.canal>1):
                self.canal-=1

    def volumenUp(self):
        if (self._estado==True):
            if (self.volumen<7):
                self.volumen+=1

    def volumenDown(self):
        if (self._estado==True):
            if (self.volumen>0):
                self.volumen-=1



