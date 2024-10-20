from abc import ABC, abstractmethod

class Personnage(ABC):
    def __new__(cls, *args, **kwargs):
        if cls == Personnage:
            raise TypeError("La classe Personnage n'est pas instanciable")
        return object.__new__(cls)
    
    def __init__(self, nom, vie, degats, experience, expRate, tour):
        self.__nom = nom
        self.__vie = vie
        self.max_vie = vie
        self.__degats = degats
        self.__experience = experience
        self.__expRate = expRate
        self.tour = tour
    
    @abstractmethod
    def frapper(self, cible: str, degats: int) -> int:
        pass
    
    @abstractmethod
    def hit_or_miss(self, degats: int) -> int:
        pass
    
    @abstractmethod
    def esquive(self) -> None:
        pass
    
    @abstractmethod
    def recoit_degats(self, degats: int) -> None:
        pass
    
    @abstractmethod
    def gagne_experience(self, exp_recue: int) -> None:
        pass
    
        
    @property
    def nom(self):
        return self.__nom
    
    @property
    def vie(self):
        return self.__vie
    
    @vie.setter
    def vie(self, value):
        if value < 0:
            self.__vie = 0
        elif value > self.max_vie:
            self.__vie = self.max_vie
        else:
            self.__vie = value
    
    @property
    def degats(self):
        return self.__degats
    
    @property
    def experience(self):
        return self.__experience
    
    @experience.setter
    def experience(self, value):
        self.__experience = value
    
    @property
    def exp_rate(self):
        return self.__expRate
    
    @exp_rate.setter
    def exp_rate(self, exp_rate):
        self.__expRate = exp_rate