from abc import ABC, abstractmethod

class Personnage(ABC):
    def __new__(cls, *args, **kwargs):
        if cls == Personnage:
            raise TypeError("La classe Personnage n'est pas instanciable")
        return object.__new__(cls)
    
    def __init__(self, nom: str, vie: int, degats: int, experience: int, expRate: float, tour: str) -> None:
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
    def nom(self) -> str:
        return self.__nom
    
    @property
    def vie(self) -> int:
        return self.__vie
    
    @vie.setter
    def vie(self, value: int) -> None:
        if value < 0:
            self.__vie = 0
        elif value > self.max_vie:
            self.__vie = self.max_vie
        else:
            self.__vie = value
    
    @property
    def degats(self) -> int:
        return self.__degats
    
    @property
    def experience(self) -> int:
        return self.__experience
    
    @experience.setter
    def experience(self, value) -> None:
        self.__experience = value
    
    @property
    def exp_rate(self) -> float:
        return self.__expRate
    
    @exp_rate.setter
    def exp_rate(self, exp_rate) -> None:
        self.__expRate = exp_rate