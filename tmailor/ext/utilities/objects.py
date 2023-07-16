from typing import List, Optional


class DomainList:
    def __init__(self, data):
        self.json: dict = data

        domains = data.get("domains", [])
        self.name: List[str] = [domain.get("name") for domain in domains]
        self.type: List[str] = [domain.get("type") for domain in domains]
        self.forward_available: List[bool] = [domain.get("forward_available") for domain in domains]
        self.forward_max_seconds: List[int] = [domain.get("forward_max_seconds") for domain in domains]


class GenerateEmail:
    def __init__(self, data):
        self.json: dict = data

        self.email: str = data.get("email")
        self.token: str = data.get("token")


class MessageList:
    class Message:
        def __init__(self):
            self.attachments: List[str] = []
            self.body_html: str = ""
            self.body_text: str = ""
            self.cc: Optional[str] = None
            self.created_at: Optional[str] = None
            self.sender: Optional[str] = None
            self.id: Optional[str] = None
            self.subject: Optional[str] = None
            self.receiver: Optional[str] = None

    def __init__(self, data):
        self.json: dict = data
        self.messages: List[MessageList.Message] = []

        if data:
            for message_data in data:
                message = MessageList.Message()
                message.attachments = message_data.get("attachments", [])
                message.body_html = message_data.get("body_html", "")
                message.body_text = message_data.get("body_text", "")
                message.cc = message_data.get("cc")
                message.created_at = message_data.get("created_at")
                message.sender = message_data.get("from")
                message.id = message_data.get("id")
                message.subject = message_data.get("subject")
                message.receiver = message_data.get("receiver")

                self.messages.append(message)
