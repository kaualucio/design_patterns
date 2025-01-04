from abc import ABC, abstractmethod

# 1. Classe abstrata de para pizzas
class Pizza(ABC):
  @abstractmethod
  def prepare(self):
    pass
  
  def bake(self):
    pass
  
  def cut(self):
    pass
  
# 2. Criação das classes concretas (criação da pizzas e suas diferentes formas de prepare, bake, cut)
class MargheritaPizza(Pizza):
  def prepare(self):
    return 'Preparando pizza Margherita com molho, tomate e manjericão.'
  
  def bake(self):
    return 'Assando pizza Margherita no forno a lenha.'
  
  def cut(self):
    return 'Cortando pizza Margherita em 6 fatias.'
  
class PepperoniPizza(Pizza):
  def prepare(self):
    return "Preparando pizza Pepperoni com molho, queijo e pepperoni."

  def bake(self):
    return "Assando pizza Pepperoni no forno elétrico."

  def cut(self):
    return "Cortando pizza Pepperoni em 8 fatias."
  
# 3. Criação do método fábrica
class PizzaFactory:
  @staticmethod
  def factory_method(pizza_type):
    if pizza_type == 'margherita':
      return MargheritaPizza()
    elif pizza_type == 'pepperoni':
      return PepperoniPizza()
    else:
      raise ValueError('Tipo de pizza desconhecido')
    
    
if __name__ == '__main__':
  factory = PizzaFactory()
  
  pizza_types = ['margherita', 'pepperoni']
  
  for pizza_type in pizza_types:
    pizza = factory.factory_method(pizza_type)
    print(pizza.prepare())
    print(pizza.bake())
    print(pizza.cut())