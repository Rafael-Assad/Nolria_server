from django.core.mail import send_mail


class ContactSevices:
    @staticmethod
    def email_sender(instance, *args, **kwargs):
        client_name = instance.name
        subject = f'{client_name} - {instance.subject}'
        message = instance.message
        client_email = instance.email
        my_email = 'rafael.assad1010@gmail.com'
        message_to_send = ContactSevices.create_email_message(message, client_email, client_name)

        return send_mail(subject = subject,
                         message = message_to_send,
                         from_email = my_email,
                         recipient_list = [client_email],
                         fail_silently = False)

    @staticmethod
    def create_email_message(message, client_emai, client_name):
        message_to_send = f"""
        cliente: {client_name}
        
        email: {client_emai}
        
        Mensagem: {message}
        """
        
        return message_to_send