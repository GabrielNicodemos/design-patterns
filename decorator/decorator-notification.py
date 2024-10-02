from abc import ABC, abstractmethod

# Interface básica (comportamento principal)
class Notification(ABC):
    @abstractmethod
    def notification(self):
        pass

# Comportamento básico
class BasicNotification(Notification):
    def notification(self):
        return "Usuário notificado pelo software"

# Decorator abstrato
class NotificationDecorator(Notification):
    def __init__(self, notification: Notification):
        self._notification = notification

    @abstractmethod
    def notification(self):
        pass

# Implementações concretas dos decoradores
class EmailDecorator(NotificationDecorator):
    def notification(self):
        return f"{self._notification.notification()} + notificado pelo email"

class SmsDecorator(NotificationDecorator):
    def notification(self):
        return f"{self._notification.notification()} + notificado pelo SMS"

class PushNotificationDecorator(NotificationDecorator):
    def notification(self):
        return f"{self._notification.notification()} + notificado pelo Push Notification"

# Uso
if __name__ == "__main__":
    # Pessoa básica
    notification = BasicNotification()
    print(notification.notification())  # Output: Usuário notificado pelo software

    # Notificando pelo email
    email_notification = EmailDecorator(notification)
    print(email_notification.notification())  # Output: Usuário notificado pelo software + noticado pelo email

    # Notificando pelo SMS
    sms_notification = SmsDecorator(email_notification)
    print(sms_notification.notification())  # Output: Usuário notificado pelo software + noticado pelo email + noticado pelo SMS

    # Notificando pelo Push Notification
    push_notification = PushNotificationDecorator(sms_notification)
    print(push_notification.notification())
    # Output: Usuário notificado pelo software + noticado pelo email + noticado pelo SMS + notificado pelo Push Notification

    # Notificando pelo Push Notification
    push_notification = PushNotificationDecorator(notification)
    print(push_notification.notification())  # Output: Usuário notificado pelo software + notificado pelo Push Notification