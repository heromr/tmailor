class DomainList:
    def __init__(self, data):
        self.json = data

        domains = data.get("domains", [])
        self.names = [domain.get("name") for domain in domains]
        self.types = [domain.get("type") for domain in domains]
        self.forward_available = [domain.get("forward_available") for domain in domains]
        self.forward_max_seconds = [domain.get("forward_max_seconds") for domain in domains]


class GenerateEmail:
    def __init__(self, data):
        self.json = data

        self.email = data.get("email")
        self.token = data.get("token")


class MessageList:
    def __init__(self, data):
        self.json = data

        self.attachments = []
        self.body_html = []
        self.body_text = []
        self.cc = []
        self.created_at = []
        self.sender = []
        self.id = []
        self.subject = []
        self.reciever = []

        if data:
            
            for messages in data:
                self.attachments.append(messages.get("attachments", []))
                self.body_html.append(messages.get("body_html", ""))
                self.body_text.append(messages.get("body_text", ""))
                self.cc.append(messages.get("cc"))
                self.created_at.append(messages.get("created_at"))
                self.sender.append(messages.get("from"))
                self.id.append(messages.get("id"))
                self.subject.append(messages.get("subject"))
                self.reciever.append(messages.get("reciever"))



