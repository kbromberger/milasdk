#!/usr/bin/env python3
"""Test script to verify async MilaApi creation works"""

import asyncio
import aiohttp
from milasdk.api import MilaApi
from milasdk import DefaultAsyncSession

async def test_async_creation():
    """Test that MilaApi can be created asynchronously"""
    try:
        session = DefaultAsyncSession(aiohttp.ClientSession(), 'test', 'test')
        api = await MilaApi.create_async(session)
        print('✅ Async MilaApi creation works!')
        print(f'Client created: {type(api._client)}')
    except Exception as e:
        print(f'❌ Error: {e}')
    finally:
        await session._session.close()

if __name__ == "__main__":
    asyncio.run(test_async_creation())
