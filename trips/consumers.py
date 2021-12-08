from channels.generic.websocket import AsyncWebsocketConsumer


class TaxiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        await super().disconnect(code)
