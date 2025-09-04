import asyncio



async def scan_port(ip, port):
    try:
        conn = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout=1)
        print(f"[+] Port {port}")
        writer.close()
        await writer.wait_closed()
    except:
        pass

async def main():
    ip = "scanme.nmap.org"
    tasks = [scan_port(ip, p) for p in range(20, 100)]
    await asyncio.gather(*tasks)

asyncio.run(main())