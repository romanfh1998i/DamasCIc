
# This is a sample Python script.
import os,random,time,threading
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy
class checkers:
    def __init__(self,tamano=8):
        self.tamano=tamano
        self.juegoAcabado=False
        self.ganador=None
        self.cuenta=0
    @staticmethod
    def opponente(color):
        return "b" if color.lower()=="w" else "W"
    def Update(self,movimiento):
        if len(movimiento)==2:
            self.cuenta+=1
        else:
            self.cuenta+=0
    @staticmethod
    def shift(tablero,posicion,rey=False,north=False):
            assert(tablero.isinbound(posicion),"shift:ficha no est en el tablero")
            Direcciondejuego=[pow(-1,north)]+[pow(-1,not north)]*rey
            movimiento=[]
            for i in Direcciondejuego:
                for j in range(-1,2,2):
                    libre=(posicion[0]+i,posicion[1]+2*j)
                    if tablero.isinbound(libre) and tablero[libre]=="_":
                        movimiento.append([posicion,libre])
            return movimiento
    @staticmethod
    def movidsimple(tablero,pos,rey=False ,norte=False):
        assert (tablero.isinbound(pos),"movida simple:ficha no esta en el tablero")
        direccionjuego=([pow(-1,norte)]+[pow(-1,not norte)]*rey)
        posicionpermidito=[]
        for i in direccionjuego:
            for j in range(-1,2,2):
                posicionoppenedte=(pos[0]+i,pos[1]+j)
                libre=(pos[0]+2 *i,pos[1]+2*j)
                if tablero.isinbound(libre).lower() not in[tablero[pos].lower(),"_"] and tablero[posicionoppenedte].lower() not in [tablero[pos].lower(),"_"]:
                    posicionpermidito.append(libre)
        return posicionpermidito
    def movimiento(self,tableroo,pos,salto,movimiento,rey=False,norte=False):
        saltosimple=self.movidsimple(tableroo,pos,rey,norte)
        if len(saltosimple)==0 and len(salto)>1:
            saltostring=''.join(map(str,salto))
            if all(saltostring not in ''.join(map(str,s))for s in movimiento):
                movimiento.append(salto)
            return
        for nuevopos in saltosimple:
            nuevotablero=copy.deepcopy(tableroo)
            nuevosalto=salto+[nuevopos]
            nuevorey=rey
            if(norte and nuevopos[0]==0) or (not norte and nuevopos[0]==tableroo-1):
                nuevorey=True
            self.movimiento(nuevotablero,nuevopos,nuevosalto,nuevorey,norte)
            self.actualizartablero(nuevotablero,pos,nuevopos)

    def movimientopermitido(self,estadodejuego):
        tablero,color=estadodejuego
        norte=color=="w"
        posiciondisco=[]
        for i,fila in enumerate(tablero.get_tablero()):
            for j,char in enumerate(fila):
                if char.lower()==color:
                    posiciondisco.append(i,j)
        movimiento=[]
        for p in posiciondisco:
            rey=tablero[p].istitle()
            salto=[p]
            self.movimiento(tablero,p,salto,movimiento,rey,norte)
        if (len(movimiento)==0):
            for p in posiciondisco:
                rey=tablero[p].istitle()
                movimiento.extend(self.shift(tablero,p,rey,norte))
        return movimiento




    @staticmethod
    def actualizartablero(tablero,posicion,nuevaposicion):
        posicion,nueva=posicion,nuevaposicion
        assert (abs(posicion[0]-nueva[0])<3,"es prefiereble utilizar otro shift no puede  hacer un movimiento legal")
        assert (tablero.isinbound(nueva),"la nueva posicion no esta en el tablero")
        if( abs(posicion[0]-nueva[0])==1):
            assert  tablero[nueva]=="_"
            tablero[nueva]=tablero[posicion]
            tablero[posicion]="_"
        elif abs(posicion[0]-nueva[0])==2:
            captura=((nueva[0]+posicion[0])/2,(nueva[1]+posicion[1])/2)
            assert tablero[nueva]=="_"
            assert tablero[captura].lower() not in [tablero[posicion].lower(),"_"]
            tablero[nueva]=tablero[posicion]
            tablero[captura]=tablero[posicion]="_"
        def actualizartablero(self,estadodejuego,movimiento):
            tablero=estadodejuego[0]

