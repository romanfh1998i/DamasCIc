import os


class Tablero:
    def __init__(self,tablero=None,tamano=8):
        assert tamano >=4 and tamano %2==0
        self.tamano=tamano
        if tablero is None:
            self.generate_board()
        elif isinstance(tablero,str):
            self.tablero=list(map(list,tablero))
        elif all(isinstance(elem,str)for elem in tablero):
            self.tablero=list(map(list,tablero))
        elif all(isinstance(element,list)for element in tablero):
            self.tablero=tablero
    def __getitem__(self, item):
        i,j=item
        return self.tablero[i][j]
    def __setitem__(self, key, value):
        x1,x2=key
        self.tablero[x1][x2]=value
    @staticmethod
    def convert_board(s,b):
        b=b.replace('\n','')
        b=b.replace(' ', '')
        return [b[i:i+s]for i in  range(0,len(b),s)]
    def generate_board(self):
        self.tablero=self.convert_board(self.tamano, """_b_b_b_b
                                        b_b_b_b_
                                        ___b_b_b
                                        b_______
                                        ________
                                        w_w_w_w_
                                        _w_w_w_w
                                        w_w_w_w_""")
    def isinbound(self,p):
        if p[0]<0 or p[0]>=len(self.tablero):
            return False
        if p[1]<0 or p[1] >=len(self.tablero[0]):
            return False
        return True
    def get_size(self):
        return self.tamano
    def get_tablero(self):
        return self.tablero