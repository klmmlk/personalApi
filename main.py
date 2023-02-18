from fastapi import FastAPI,Response
from fastapi.exceptions import StarletteHTTPException
from znzmo.znzup import znzmo
import json
app = FastAPI()
app.include_router(znzmo)


@app.exception_handler(StarletteHTTPException)
async def not_found(request, exc):
    return Response(
        json.dumps(
            {"code": 404,
             "message": f"您要找的页面 {request.url} 去火星了。"}),
        status_code=404
    )

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='127.0.0.1', port=8800, reload=True)
