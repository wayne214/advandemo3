import concurrent.futures
import requests
import threading
import time


# 在 download_one() 函数中，我们使用的 requests.get() 方法是线程安全的（thread-safe），
# 因此在多线程的环境下，它也可以安全使用，
# 并不会出现 race condition 的情况。
def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # executor.map(download_one, sites)
        to_do = []
        for site in sites:
            # 当我们执行
            # executor.submit(func)
            # 时，它便会安排里面的
            # func()
            # 函数执行，并返回创建好的
            # future
            # 实例，以便你之后查询调用。
            future = executor.submit(download_one, site)
            to_do.append(future)

        # as_completed(fs)，则是针对给定的future迭代器fs，在其完成后，返回完成后的迭代器。
        for future in concurrent.futures.as_completed(to_do):
            future.result()


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
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} site in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
