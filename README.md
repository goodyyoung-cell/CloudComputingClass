# CloudComputingClass — 개인 소개 & 프론트·백엔드 연동 실습

클라우드 컴퓨팅 실습 과제입니다. 개인 소개 페이지와, 프론트엔드에서 백엔드 API를 호출하는 간단한 연동 실습으로 구성되어 있습니다.

## 프로젝트 소개

- **개인 소개 페이지**: 본인 소개를 담은 정적 HTML 페이지 (Vercel 배포)
- **연동 실습**: 프론트엔드(Vercel)에서 백엔드(Render, FastAPI) API를 호출해 인사 메시지를 받아 화면에 표시
- 소개 페이지와 실습 페이지는 서로 링크로 연결되어 있습니다.

## 주요 구성

```
CloudComputingClass/
├── frontend/            # Vercel에 배포하는 정적 프론트엔드
│   ├── index.html       # 개인 소개 페이지
│   └── practice.html    # 프론트–백엔드 연동 실습 페이지
├── backend/             # Render에 배포하는 FastAPI 백엔드
│   ├── main.py          # API 서버 (/, /api/hello, /api/greet)
│   └── requirements.txt # 의존성 (fastapi, uvicorn)
└── README.md
```

### 백엔드 API

| 메서드 | 경로 | 설명 |
| --- | --- | --- |
| GET | `/` | 서버 동작 확인 |
| GET | `/api/hello?name=이름` | 이름을 받아 인사 메시지 반환 (프론트에서 사용) |
| POST | `/api/greet` | JSON 본문 `{"name": "이름"}`으로 인사 메시지 반환 |

FastAPI는 `/docs` 경로에서 Swagger UI를 자동 제공합니다.

## 배포 주소

- **GitHub 저장소**: https://github.com/goodyyoung-cell/CloudComputingClass
- **Vercel (프론트엔드)**: https://cloud-computing-class.vercel.app/
- **백엔드 Swagger UI (Render)**: https://cloudcomputingclass.onrender.com/docs
- **백엔드 기본 주소 (Render)**: https://cloudcomputingclass.onrender.com

## 로컬 실행 방법

### 백엔드
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
# http://127.0.0.1:8000/docs 에서 Swagger UI 확인
```

### 프론트엔드
`frontend/practice.html`의 `API_BASE` 값을 백엔드 주소로 설정한 뒤, `frontend/index.html`을 브라우저로 엽니다.

## 배포 개요

- **백엔드(Render)**: Root Directory `backend`, Start Command `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **프론트엔드(Vercel)**: Root Directory `frontend` (정적 파일 그대로 배포)
- 배포 후 `frontend/practice.html`의 `API_BASE`를 Render 백엔드 주소로 변경

---
작성: 손영훈 (IMMS / Salesforce) · 클라우드 컴퓨팅 실습
