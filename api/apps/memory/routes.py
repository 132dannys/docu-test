from flask_restful import Resource, reqparse, inputs

from .models import MemoryAlarm
from settings.database import connect


parser = reqparse.RequestParser()
parser.add_argument("usage", type=int, required=True, help="This is required")
parser.add_argument("created_at", type=inputs.datetime_from_iso8601, required=True, help="This is required")


class MemoryView(Resource):
    def get(self):
        memory_alarms = MemoryAlarm.objects.all()
        return [memory_alarm.to_json() for memory_alarm in memory_alarms], 200

    def post(self):
        data = parser.parse_args()
        memory_alarm = MemoryAlarm(**data)
        memory_alarm.save()
        return {
            "message": "Memory Alarm created successfully",
            "memory_alarm": memory_alarm.to_json()
        }, 201


class SingleMemoryView(Resource):
    def put(self, memory_alarm_id):
        args = parser.parse_args()
        memory_alarm = MemoryAlarm.objects(id=memory_alarm_id).first()
        if memory_alarm:
            memory_alarm.usage = args["usage"]
            memory_alarm.created_at = args["created_at"]
            memory_alarm.save()
            return {"message": "Memory Alarm updated successfully"}, 200
        return {"message": "Memory Alarm not found"}, 404
