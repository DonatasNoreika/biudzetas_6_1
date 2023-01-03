from modules.pajamu_irasas import PajamuIrasas
from modules.islaidu_irasas import IslaiduIrasas
import pickle


class Biudzetas:
    def __init__(self):
        self.zurnalas = self.nuskaityti_is_failo()

    def prideti_pajamu_irasa(self, suma, siuntejas, info):
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_i_failas()

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga, info):
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga, info)
        self.zurnalas.append(irasas)
        self.irasyti_i_failas()

    def gauti_balansa(self):
        bendrasuma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                bendrasuma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                bendrasuma -= irasas.suma
        return bendrasuma

    def gauti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)

    def nuskaityti_is_failo(self):
        try:
            with open("biudzetas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def irasyti_i_failas(self):
        with open("biudzetas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)
