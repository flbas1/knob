from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
import uvicorn
import asyncio
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

clients: list[WebSocket] = []


@app.get("/")
async def index():
    from fastapi.responses import FileResponse
    return FileResponse("static/index.html")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    clients.append(websocket)

    print(f"Browser connected. Clients={len(clients)}")

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:

        print("Browser disconnected.")

        clients.remove(websocket)

        

async def render(payload: dict):

    print("RENDER:", payload)

    for client in clients.copy():
        try:
            await client.send_json(payload)
        except Exception as e:
            print("Websocket send failed:", e)
            clients.remove(client)

 


async def tcp_server(reader, writer):

    address = writer.get_extra_info("peername")

    print(f"Device connected: {address}")

    while True:

        data = await reader.readline()

        if not data:
            break

        payload = json.loads(data.decode())

        print("DEVICE PAYLOAD:")
        print(payload)

        await render(payload)

    writer.close()


async def start_tcp():

    server = await asyncio.start_server(
        tcp_server,
        "0.0.0.0",
        5000
    )

    print("TCP device server listening on 5000")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":

    async def main():

        tcp_task = asyncio.create_task(start_tcp())

        config = uvicorn.Config(
            app,
            host="0.0.0.0",
            port=8080
        )

        server = uvicorn.Server(config)

        await asyncio.gather(
            tcp_task,
            server.serve()
        )


    asyncio.run(main())