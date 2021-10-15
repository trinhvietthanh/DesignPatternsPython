from abc import ABC, abstractmethod


class Chair(ABC):
    """
    Abstract Product Chair
    """
    @abstractmethod
    # Interface
    def hasLegs(self):
        pass

    @abstractmethod
    def sitOn(self):
        pass

class ChairVictorian(Chair):
    # Abstract Method of the Chair base class
    def hasLegs(self):
        print("Chair Victorian - Legs Created")
    # Abstract Method of the Chair base class    
    def sitOn(self):
        print("Chair Victorian - Sit Created")

    def feature1Victorian(self):
        print("Chair Victorian - Feature 1 created")

class ChairModern(Chair):
    # Abstract Method of the Chair base class
    def hasLegs(self):
        print("Chair Modern - Legs Created")
    # Abstract Method of the Chair base class
    def sitOn(self):
        print("Chair Modern - Sit Created")

    def feature2Victorian(self):
        print("Chair Modern - Feature 2created")

class Table(ABC):
    """
    Abstract Product Table
    """
    @abstractmethod
    def Color(self):
        pass

    @abstractmethod
    def Material(self):
        pass

class TableVictorian:
    """
    Concrete Product
    """

    #Abstract Method of the Table base class
    def Color(self):
        print("Table Victorian - Color Red")

    #Abstract Method of the Table base class
    def Material(self):
        print("Material Wood")

class TableModern:
    """
    Concrete Product
    """

    #Abstract Method of the Table base class
    def Color(self):
        print("Table Modern - Color White")
    #Abstract Method of the Table base class
    def Material(self):
        print("Material Metal")

    def hasGlass(self):
        print("Has Glass - Yes")

class Sofa(ABC):
    """
    Abstract Product Sofa
    """
    @abstractmethod
    def hasLegs(self):
        pass

    @abstractmethod
    def sitOn(self):
        pass
    
    @abstractmethod
    def size(self):
        pass

class SofaVictorian(Sofa):
    """
    Concrete Product
    """

    #Abstract Method of the Sofa base class
    def hasLegs(self):
        print("Sofa Victorian - Legs created")
    
    #Abstract Method of the Sofa base class
    def sitOn(self):
        print("Sofa Victorian - Sit on board")

    #Abstract Method of the Sofa base class
    def size(self):
        print("Sofa Victorian - Size Lager")


class SofaModern(Sofa):
    """
    Concrete Product
    """     

    #Abstract Method of the Sofa base class
    def hasLegs(self):
        print("Sofa Modern - Legs created")
    
    #Abstract Method of the Sofa base class
    def sitOn(self):
        print("Sofa Modern - Sit on low")
    
    #Abstract Method of the Sofa base class
    def size(self):
        print("Sofa Modern - Size Medium")

class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self)->Chair:
        pass
    @abstractmethod
    def create_table(self)->Table:
        pass
    @abstractmethod
    def create_sofa(self)->Sofa:
        pass

class FurnitureModernFactory(AbstractFactory):
    """
    The Concrete Factory
    """
    def create_chair(self):
        return ChairModern()

    def create_table(self):
        return TableModern()

    def create_sofa(self):
        return SofaModern()

class FurnitureVictorianFactory(AbstractFactory):
    """
    The Concrete Factory
    """
    def create_chair(self):
        return ChairVictorian()

    def create_table(self):
        return TableVictorian()

    def create_sofa(self):
        return SofaVictorian()

def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    chair = factory.create_chair()
    table = factory.create_table()
    sofa = factory.create_sofa()
    chair.hasLegs()
    chair.sitOn()
    table.Material()
    sofa.size()

if __name__ == "__main__":

    for factory in (FurnitureModernFactory(), FurnitureVictorianFactory()):
        print("____Client Order____")
        client_code(factory)