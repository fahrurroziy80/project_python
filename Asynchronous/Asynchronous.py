import asyncio
import socket

async def scan_port(ip, port):
    try:
        conn = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout=1)
        print(f"[+] Port {port} terbuka")
        writer.close()
        await writer.wait_closed()
    except:
        pass

async def main():
    ip = "scanme.nmap.org"  # target bisa diganti
    tasks = [scan_port(ip, port) for port in range(20, 1025)]
    await asyncio.gather(*tasks)

asyncio.run(main())
