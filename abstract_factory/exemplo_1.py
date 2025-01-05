# Classes dos produtos abstratos
class Button: 
  def render(self):
    raise NotImplementedError
  
  def on_click(self):
    return 'O botão foi clicado'
  
class TextBox: 
  def render(self):
    raise NotImplementedError
  
  def change_text(self, text: str):
    return f'O texto da textbox foi alterado para: {text}'
  
class Menu:
  def render(self):
    raise NotImplementedError

  def open_menu(self):
   return 'O menu foi aberto'
    
  def close_menu(self):
   return 'O menu foi fechado'
    
# Classes dos produtos concretos
class LightButton(Button):
  def render(self):
    return 'A cor do botão preto'
  
class LightTextBox(TextBox):
  def render(self):
    return 'A cor do texto preto'
  
class LightMenu(Menu):
  def render(self):
    return 'A cor do menu preto'
  
class DarkButton(Button):
  def render(self):
    return 'A cor do botão branco'
  
class DarkTextBox(TextBox):
  def render(self):
    return 'A cor do texto branco'
  
class DarkMenu(Menu):
  def render(self):
    return 'A cor do menu branco'
  
# Classes das fábricas abstratas
class GUIFactory:
  def create_button(self):
    raise NotImplementedError
  
  def create_textbox(self):
    raise NotImplementedError
  
  def create_menu(self):
    raise NotImplementedError
      
# Classes das fábricas concretas
class LightModeFactory(GUIFactory):
  def create_button(self):
    return LightButton()
  
  def create_textbox(self):
    return LightTextBox()
  
  def create_menu(self):
    return LightMenu()
    
class DarkModeFactory(GUIFactory):
  def create_button(self):
    return DarkButton()
  
  def create_textbox(self):
    return DarkTextBox()
  
  def create_menu(self):
    return DarkMenu()
    
def client_code(factory: GUIFactory):
  button = factory.create_button()
  textbox = factory.create_textbox()
  menu = factory.create_menu()
  print(button.render())
  print(button.on_click())
  print(textbox.render())
  print(textbox.change_text('Novo texto do textbox'))
  print(menu.render())
  print(menu.open_menu(), menu.close_menu())
  
if __name__ == '__main__':
  lightmode = LightModeFactory()
  print("Criando LightMode:")
  client_code(lightmode)
  
  print('-'*50)
  
  darkmode = DarkModeFactory()
  print("Criando DarkMode:")
  client_code(darkmode)