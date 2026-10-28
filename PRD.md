# PRD — LEC 13 / Drill 11: 소년 상태 머신과 AutoRun

- 작성일: 2026-10-28
- 대상 폴더: `C:\Users\tedu0\Desktop\대학\2D-GP\lec 13`
- 작업 저장소: `https://github.com/bbbboxvader/lec-13`
- 이전 원본: `C:\Users\tedu0\2DGP-2023180016`
- 구현 위치: 이 `lec 13` 저장소의 루트 폴더
- 상태: 구현 및 동작 검증 완료

## 1. 목표

Pico2D 화면의 소년을 `transitions.Machine`으로 제어한다. IDLE, SLEEP,
RUN을 유지하면서 별도의 `AutoRun` 상태 클래스를 추가한다. 사용자는 A키로
자동 이동을 시작하고, 방향키로 일반 달리기에 복귀할 수 있어야 한다.

## 2. 실행 환경

- Python과 `pico2d`, `transitions` 라이브러리를 사용한다.
- 실제 실행 검증 환경은 Windows의 Python 3.14이다.
- 기본 캔버스는 800×600이며, 이동 경계는 실제 캔버스 너비로 계산한다.
- 이미지는 `animation_sheet.png`, `grass.png`를 사용한다.
- 애니메이션은 8프레임을 10 FPS로 반복한다.

```powershell
python -m pip install -r requirements.txt
python main.py
```

명령은 이 문서가 있는 `lec 13` 폴더에서 실행한다.

