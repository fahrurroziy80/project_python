"""contoh"""
import asyncio
#
# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')
#
# asyncio.run(main())

async def halo(nama):
    print(f"Hallo {nama}")
    await asyncio.sleep(2)
    print(f"Selesai menyapa {nama}")

async def main():
    await asyncio.gather(
        halo('alica'),
        halo('bab'),
        halo('ala')
    )

asyncio.run(main())
