from mongoengine import Document, fields

from settings.database import connect


class MemoryAlarm(Document):
    usage = fields.IntField()
    created_at = fields.DateTimeField()

    def to_json(self):
        return {
            "id": str(self.id),
            "usage": self.usage,
            "created_at": f"{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        }
