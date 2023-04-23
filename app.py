import asyncio
import configparser
import time

import aiofiles
from colorama import Fore

from loguru import logger
from pyrogram import Client
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied, FloodWait

config = configparser.ConfigParser()
config.read('config.ini')

API_ID = config.get('pyrogram', 'API_ID')
API_HASH = config.get('pyrogram', 'API_HASH')
TIME_SLEEP = config.get('pyrogram', 'TIME_SLEEP')


async def check_nick():
    async with aiofiles.open('nicks.txt', encoding='utf-8') as file:
        nicks_list = [nick.replace('\n', '') for nick in await file.readlines()]

    async with Client('account', API_ID, API_HASH) as app:
        for nick in nicks_list:
            try:
                await app.get_users(nick)
                logger.error(f'@{nick} - busy')

            except UsernameNotOccupied:
                logger.info(f'@{nick} - availabl')
                async with aiofiles.open('available_nicks.txt', 'a', encoding='utf-8') as file:
                    await file.write(nick + '\n')

            except UsernameInvalid:
                logger.error(f'@{nick} - incorrect nickname')

            except IndexError:
                logger.error(f'@{nick} - busy')

            except FloodWait as flood:
                converted_time = time.strftime(
                    '%H часов %M минут %S секунд',
                    time.gmtime(flood.value)
                )
                print(Fore.RED + f'Too many requests! Waiting: {converted_time}')
                await asyncio.sleep(flood.value)

            await asyncio.sleep(int(TIME_SLEEP))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(check_nick())
