from hubs.models import Hub


class HubService:
    """
    Сервис Хабов
    """

    @staticmethod
    async def get_hubs() -> list[Hub]:
        return [hub async for hub in Hub.objects.all()]


hub_service: HubService = HubService()
