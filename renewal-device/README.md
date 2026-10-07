# BR-A 갱신 장치

## 목적
13주 기록을 `input/records.json`에 넣고 실행하면 공개 페이지에 사용할 숫자와 후보 데이터를 `output/summary.json`으로 다시 만듭니다.

## 실행
Windows PowerShell 또는 VS Code 터미널에서 이 폴더로 이동한 뒤:

```bash
py update.py
```

## 통과 확인 1 - 같은 입력, 같은 결과
1. `py update.py` 실행
2. 화면에 표시되는 `동일 입력 확인용 해시`를 기록
3. 아무 파일도 수정하지 않고 다시 `py update.py` 실행
4. 두 해시가 같으면 통과

## 통과 확인 2 - 새 기록 반영
1. `input/records.json`의 `ritual.morning` 값을 36에서 37로 변경
2. `py update.py` 실행
3. `output/summary.json`의 `morning_records`가 37이면 통과
4. 테스트 후 원래 실제 숫자로 되돌립니다.

## 입력/출력
- 입력: `input/records.json`
- 실행: `update.py`
- 출력: `output/summary.json`

## 개인정보
본인 이름 외 다른 사람의 실명, 연락처, 비밀번호, 토큰, API 키를 넣지 않습니다.

## Windows 실행 명령
Windows PowerShell에서는 아래 명령을 우선 사용합니다.

```powershell
py update.py
```

`py` 명령이 없는 환경에서는 Python이 PATH에 등록되어 있다면 다음 명령도 사용할 수 있습니다.

```powershell
python update.py
```
