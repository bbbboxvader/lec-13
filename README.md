# LEC 13: IDLE / SLEEP / RUN 상태 머신

`transitions.Machine`으로 구현한 소년 상태 머신 실습입니다.

## 실행

이 폴더에서 PowerShell 터미널을 열어 실행합니다.

```powershell
python -m pip install -r requirements.txt
python main.py
```

VS Code에서는 `main.py`를 실행합니다. 실행하는 Python 환경에 `pico2d`와
`transitions`가 설치되어 있어야 합니다.

## 조작

- IDLE에서 5초가 지나면 SLEEP으로 전환합니다.
- SLEEP에서 Space를 누르면 IDLE로 돌아가고 5초 타이머가 다시 시작됩니다.
- IDLE 또는 SLEEP에서 왼쪽/오른쪽 방향키를 누르면 RUN으로 전환합니다.
- 방향키를 놓으면 IDLE로 돌아갑니다. 두 방향키를 함께 누른 경우에는
  가장 최근에 누른 방향으로 달리고, 한쪽을 놓으면 남은 방향으로 달립니다.
- 소년은 화면 밖으로 나가지 않습니다.
- Escape 또는 창 닫기로 종료합니다.

## 파일

- `boy.py`: 상태 머신, 애니메이션, 키 입력, 이동과 화면 경계 처리
- `grass.py`: 잔디 객체
- `main.py`: 게임 루프와 이벤트 전달
- `animation_sheet.png`, `grass.png`: 실행에 필요한 이미지
- `requirements.txt`: Python 의존성
- `idle_state.md`: 최종 상태 다이어그램
- `commit_history.md`: 이번 작업의 로컬 커밋 15개 목록

원본 저장소는 `C:\Users\tedu0\2DGP-2023180016`에 있습니다.
이 폴더에는 실행용 파일과 커밋 목록을 복사했습니다.
