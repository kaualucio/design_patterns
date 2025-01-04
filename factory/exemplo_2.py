from abc import ABC, abstractmethod

# 1. Classe abstrata para as notificações
class Notification(ABC):
  
  @abstractmethod
  def send(self, recipient, message):
    pass
  
# 2. Implementação concretas das notificações
class EmailNotification(Notification):
  
  def send(self, recipient, message):
    return f"Enviando E-mail para {recipient} com a mensagem: {message}"
  
class SMSNotification(Notification):
  def send(self, recipient, message):
    return f"Enviando SMS para {recipient} com a mensagem: {message}"

class PushNotification(Notification):
  def send(self, recipient, message):
    return f"Enviando Push Notification para {recipient} com a mensagem: {message}"

# 3. Fábrica com Registro Interno
class NotificationFactory:
  _registry = {}
  
  @classmethod
  def register_notification(cls, channel, notification_class):
    # Registra uma nova classe de notificação na fábrica
    cls._registry[channel] = notification_class
  
  @classmethod
  def factory_method(cls, channel):
    notification_class = cls._registry.get(channel)
    if not notification_class:
      raise ValueError(f'Canal de notificação desconhecido: {channel}')
    return notification_class()
  
# Registrando os canais de notificação
NotificationFactory.register_notification('email', EmailNotification)
NotificationFactory.register_notification('sms', SMSNotification)
NotificationFactory.register_notification('push', PushNotification)

class NotificationManager:
  def __init__(self):
    self.factory = NotificationFactory()
  
  def create_notification(self, channel, recipient, message):
    
    try:
      notification = self.factory.factory_method(channel)
      return notification.send(recipient, message)
    except ValueError as e:
      return str(e)
    
if __name__ == '__main__':
  manager = NotificationManager()
  
  notifications = [
      {"channel": "email", "recipient": "user@example.com", "message": "Bem-vindo ao nosso sistema!"},
      {"channel": "sms", "recipient": "+551199999999", "message": "Seu pedido foi enviado!"},
      {"channel": "push", "recipient": "Device123", "message": "Você recebeu uma nova mensagem."},
      {"channel": "unknown", "recipient": "test", "message": "Teste de canal desconhecido."},
  ]
  
  for notification in notifications:
    response = manager.create_notification(
      channel=notification['channel'],
      recipient=notification['recipient'],
      message=notification['message'],
    )
    print(response)
    
