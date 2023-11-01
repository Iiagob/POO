class Pessoa:
    def __init__(self,nome,idade,peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.falando=False
        self.dormindo=False

    def comer(self):
        if self.comendo == True:
            print(f"{self.nome} não pode comer porque já está comendo")
        elif self.dormindo==True:
            print(f"{self.nome} não pode comer porque  esta dormindo")
        elif self.falando == True:
            print(f"{self.nome} não pode comer porque está falando")
        else:
            print(f'{self.nome} foi comer!')
            self.comendo =True

    def falar(self):
        if self.falando == True:
            print(f"{self.nome} não pode falar porque já está falando")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar porque esta dormindo")
        elif self.comendo == True:
            print(f"{self.nome} não pode falar porque está comendo")
        else:
            print(f'{self.nome} foi falar!')
            self.falando = True

    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} não pode dormir porque já está dormindo")
        elif self.falando == True:
            print(f"{self.nome} não pode dormir porque esta falando")
        elif self.comendo == True:
            print(f"{self.nome} não pode dormir porque está comendo")
        else:
            print(f'{self.nome} foi dormir!')
            self.dormindo = True


    def apresentar(self):
        print(f"Olá!!! Meu nome é {self.nome}, atualmente tenho {self.idade} anos e peso {self.peso}KG")
