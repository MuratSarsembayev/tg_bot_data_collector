import asyncio
import asyncpg


class Database:
    def __init__(self, database, user, password, host, port, loop: asyncio.AbstractEventLoop):
        """Создание connection pool для подключения к базе данных. Connection Pool вроде как работает быстрее"""
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(database=database, user=user, password=password, host=host, port=port))

