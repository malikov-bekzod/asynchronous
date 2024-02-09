import asyncio





async def task_1():
    await asyncio.sleep(11)
    print("task 1 completed")

async def task_2():
    await asyncio.sleep(2)
    print("task 2 completed")

async def task_3():
    await asyncio.sleep(1)
    print("task 3 completed")

async def task_4():
    await asyncio.sleep(5)
    print("task 4 completed")

async def task_5():
    await asyncio.sleep(6)
    print("task 5 completed")

async def task_6():
    await asyncio.sleep(4)
    print("task 6 completed")

async def task_7():
    await asyncio.sleep(7)
    print("task 7 completed")

async def task_8():
    await asyncio.sleep(5)
    print("task 8 completed")

async def task_9():
    await asyncio.sleep(1)
    print("task 9 completed")

async def task_10():
    await asyncio.sleep(10)
    print("task 10 completed")

async def task_11():
    await asyncio.sleep(5)
    print("task 11 completed")

async def task_12():
    await asyncio.sleep(4)
    print("task 12 completed")

async def task_13():
    await asyncio.sleep(8)
    print("task 13 completed")

async def task_14():
    await asyncio.sleep(9)
    print("task 14 completed")

async def task_15():
    await asyncio.sleep(7)
    print("task 15 completed")

async def task_16():
    await asyncio.sleep(10)
    print("task 16 completed")

async def task_17():
    await asyncio.sleep(11)
    print("task 17 completed")

async def task_18():
    await asyncio.sleep(8)
    print("task 18 completed")

async def task_19():
    await asyncio.sleep(6)
    print("task 19 completed")

async def task_20():
    await asyncio.sleep(10)
    print("task 20 completed")

async def main():
    await asyncio.gather(task_1(), task_2(), task_3(), task_4(), task_5(), task_6(), task_7(), task_8(), task_9(), task_10()
                         , task_11(), task_12(), task_13(), task_14(), task_15(), task_16(), task_17(), task_18(), task_19(), task_20())

asyncio.run(main())