# 并发编程之Asyncio
import asyncio
import aiohttp
import time


async def download_one(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                 AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
    }
    async with aiohttp.ClientSession(
            headers=header, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))


async def download_all(sites):
    task = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*task)


def main():
    sites = ['https://en.wikipedia.org/wiki/Portal:Arts', 'https://en.wikipedia.org/wiki/Portal:History',
             'https://en.wikipedia.org/wiki/Portal:Society', 'https://en.wikipedia.org/wiki/Portal:Biography',
             'https://en.wikipedia.org/wiki/Portal:Mathematics', 'https://en.wikipedia.org/wiki/Portal:Technology',
             'https://en.wikipedia.org/wiki/Portal:Geography', 'https://en.wikipedia.org/wiki/Portal:Science',
             'https://en.wikipedia.org/wiki/Computer_science',
             'https://en.wikipedia.org/wiki/Python_(programming_language)',
             'https://en.wikipedia.org/wiki/Java_(programming_language)', 'https://en.wikipedia.org/wiki/PHP',
             'https://en.wikipedia.org/wiki/Node.js', 'https://en.wikipedia.org/wiki/The_C_Programming_Language',
             'https://en.wikipedia.org/wiki/Go_(programming_language)'
             ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()

