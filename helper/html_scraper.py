import os
import asyncio
from .asyncioPoliciesFix import decorator_asyncio_fix
from constants.headers import HEADER_AIO

HTTP_PROXY = os.environ.get("HTTP_PROXY", None)

class Scraper:
    @decorator_asyncio_fix
    async def _get_html(self, session, url, force_dont_use_proxy):
        try:
            async with session.get(
                url,
                headers=HEADER_AIO,
                proxy=None if force_dont_use_proxy else HTTP_PROXY
            ) as r:
                return await r.text(encoding="ISO-8859-1")
        except:
            return None

    async def get_all_results(self, session, url, force_dont_use_proxy=False):
        return await asyncio.gather(asyncio.create_task(self._get_html(session, url, force_dont_use_proxy)))
