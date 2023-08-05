from datetime import datetime

import requests

from . import exceptions


class Poopmap:
    def __init__(self):
        self.session = requests.Session()

        self.session.headers = {
            "user-agent": "Dart/2.14 (dart:io)"
        }

        self.device_id = None
        self.token = None

        self._get_device_data()

    def _get_device_data(self):
        data = self.session.post(
            'https://api.poopmap.net/api/v1/devices',
            json={}
        )
        if data.status_code != 200:
            raise exceptions.PoopHTTPException(f"Devices: Failed to get device data: {data.text}")
        body = data.json()
        self.device_id = body['device']['id']
        self.token = body['device']['token']

    def drop_a_poop(self, longitude: float, latitude: float):
        data = self.session.post(
            'https://api.poopmap.net/api/v1/poops',
            headers={
                "authorization": f"Token token={self.token}"
            },
            json={
                "latitude": longitude,
                "longitude": latitude,
                "original_latitude": None,
                "original_longitude": None,
                "created_at": datetime.now().isoformat(),
                "app_version": "4.9.5",
                "sticker": "1"
            }
        )
        if data.status_code != 200:
            raise exceptions.PoopHTTPException(f"Devices: Failed to drop a poop: {data.text}")

        return data.json()
