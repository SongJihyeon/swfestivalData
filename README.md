# SW festival 데이터 시각화<br>
<br>
-2020-2(4학기 때) 한동대학교에서 열렸던 SW Festival 데이터 시각화 부문 장려상 수상-<br>
=> 팀 과제 수행(with. 권혁찬, 김다영)<br>

**[대회의 목적]**<br>
: 제공된 유동인구 및 매출 데이터로부터 인구 밀집/이동 패턴<br>
: 매출 흐름에 대한 새로운 인사이트를 찾고<br>
: 새로운 가치 창출에 대한 실마리 발굴<br>
<br>
**[데이터셋 항목 정리]**<br>
*유동인구 및 매출 데이터*
- 년월일
- 24시간대 구분 코드
- 성별
- 연령대 구분 코드 : 우리가 원하는 연령대만 뽑아서 보기 가능. 예를들면 20대 클럽?
- 행정동 코드 : 이걸로 지역 추리 가능
- 인구수
*SeoulFloating.csv*
- 날짜
- 시간
- birth year
- 성별
- 지역
- 구
- 유동인구
*card.csv*
- 카드 사용 내역 접수 일자
- 가맹점 위치 기준 행정동 코드
- 가맹점 위치 기준 행정동 명
- 가맹점 업종 코드
- 가맹점 업종명
- 매출발생건수
- 매출발생금액

**최종 목표!**
유동인구랑 매출이랑 관련이 없는 분야를 찾는다. 
뛰는 업종: 지금 현재 업종별 결제 금액이 높은 업종
뛰는 업종이 많지 않은 구에서 그 뛰는 업종을 진행해라.(인구 대비)

**보완점**
코로나 시기에 있었던 카드 관련 데이터를 가져와 구별로 뽑아낸 후, 구별 카드 사용량의 증가와 감소에 대해 시각화를 했으나,
우리가 예상했던 것과는 다르게 코로나 전,후 매출 차이가 극명하지 않았고, 지도 형식으로 시각화를 진행하였으나 객관적인 지표가 되지는 못했던 것 같다.
이번에 했던 것과는 다르게 다음번 시각화 과정에서는 결과가 더 객관적으로 보여질 수 있는 그래프를 사용해보는 것이 해결책이 될 수 있을 것 같다.
