from typing import List

from src.entity.proxy_entity import ProxyEntity
from src.log.logger import logger


class AbsSpider(object):

    def __init__(self, name='unknown') -> None:
        self._name = name

    async def crawl(self):
        logger.info(f'{self._name}开始爬取...')
        try:
            return await self.do_crawl()
        except Exception as e:
            logger.exception(f'{self._name}爬取失败:e:{e}')
        return []

    async def do_crawl(self) -> List[ProxyEntity]:
        raise NotImplementedError

