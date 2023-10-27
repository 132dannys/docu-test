import time
import json
from datetime import datetime

import httpx
import psutil

memory_threshold = 500

api_url = "http://127.0.0.1:8080/api/v1/memories"


def check_memory_usage():
    while True:
        memory_usage = psutil.virtual_memory().used / (1024 ** 2)

        if memory_usage > memory_threshold:
            with httpx.Client() as client:
                headers = {"Content-Type": "application/json"}
                response = client.post(api_url,
                                       data=json.dumps({"usage": memory_usage,
                                                        "created_at": datetime.now().isoformat(),
                                                        }),
                                       headers=headers)
                if response.status_code == 201:
                    print(f"Memory Alarm created successfully. Used memory: {memory_usage}")
                else:
                    print(f"ERROR! Status code: {response.status_code}")

        time.sleep(5)


if __name__ == "__main__":
    check_memory_usage()
