from Interface.ApiClient import ApiClient


class TestManager:
    def __init__(self, api_token):
        self.host = "https://sara-bed.devsuperannotate.com"
        self.api_client = ApiClient(api_token)

    async def log_test_result(self, session_id, result):
        test_api_url = self.host + '/healthcheck'
        await self.api_client.get(test_api_url)
