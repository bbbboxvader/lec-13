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

