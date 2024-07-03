from datetime import datetime
from Interface.ApiClient import ApiClient


class SessionManager:
    def __init__(self, api_token):
        self.host = "https://sara-bed.devsuperannotate.com"
        self.api_client = ApiClient(api_token)
        self.custom_data = {}

    async def start_session(self):
        start_api_url = self.host + '/healthcheck'
        self.custom_data['start_time'] = datetime.now().isoformat()
        response_data = await self.api_client.get(start_api_url)
        self.custom_data['session_id'] = response_data.get('session_id')
        print("Session started successfully.")

    async def finish_session(self, exitstatus):
        finish_api_url = self.host + '/healthcheck'
        self.custom_data['end_time'] = datetime.now().isoformat()
        self.custom_data['exitstatus'] = exitstatus
        await self.api_client.get(finish_api_url)
        print("Session data successfully stored.")
