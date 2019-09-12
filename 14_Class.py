class Televisao:
    def __init__(self , min, max):
        self.ligada = False
        self.canal = 2
        self.canal_max = max
        self.canal_min = min
    def muda_canal_para_baixo(self):
        if (self.canal - 1 >= self.canal_min):
            self.canal -= 1
            
        
    def muda_canal_para_cima(self):
        if (self.canal + 1 <= self.canal_max):
            self.canal +=1
        
tv = Televisao(1,99)
tv.muda_canal_para_baixo()
tv.muda_canal_para_baixo()
tv_sala = Televisao(1,500)
print (tv.canal)
