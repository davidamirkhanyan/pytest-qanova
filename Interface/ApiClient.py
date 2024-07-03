import httpx
import aiohttp
import asyncio

class ApiClient:
    def __init__(self, api_token):
        self.api_token = api_token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_token}'
        }

    async def get(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()

    async def post(self, url, data):
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()

    async def put(self, url, data):
        async with httpx.AsyncClient() as client:
            response = await client.put(url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()

    async def delete(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        
    async def fire_get(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(f"Request sent to {url} - Status: {response.status}")
                # Optionally process the response here, but this would wait for it
                # data = await response.text()
    
    def send_fire_get(self, url):
        loop = asyncio.get_event_loop()
        loop.create_task(self.fire_get(url))

    
