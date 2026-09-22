"""
클라우드 컴퓨팅 실습 - FastAPI 백엔드
이름을 받아 인사 메시지를 돌려주는 간단한 API 서버입니다.
Render에 배포하며, /docs 에서 Swagger UI로 API를 테스트할 수 있습니다.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="클라우드 컴퓨팅 실습 API",
    description="이름을 입력하면 인사 메시지를 돌려주는 간단한 백엔드입니다.",
    version="1.0.0",
)

# 프론트엔드(Vercel)에서 호출할 수 있도록 CORS 허용
# 실습이므로 모든 출처를 허용합니다. (운영 환경에서는 특정 도메인만 허용 권장)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GreetRequest(BaseModel):
    name: str


@app.get("/")
def root():
    """서버 동작 확인용 기본 엔드포인트"""
    return {"message": "백엔드 서버가 정상 동작 중입니다. /docs 에서 API를 확인하세요."}


@app.get("/api/hello")
def hello(name: str = "손영훈"):
    """
    쿼리 파라미터로 이름을 받아 인사 메시지를 돌려줍니다.
    예: /api/hello?name=홍길동
    """
    return {"message": f"안녕하세요, {name}님! 클라우드 컴퓨팅 실습에 오신 것을 환영합니다."}


@app.post("/api/greet")
def greet(req: GreetRequest):
    """
    JSON 본문(body)으로 이름을 받아 인사 메시지를 돌려줍니다.
    예: {"name": "홍길동"}
    """
    return {"message": f"안녕하세요, {req.name}님! 반갑습니다."}
