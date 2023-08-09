<details>
<summary>Titanic From Disaster</summary>

#### DDA
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | --- |
| survival | Survival | 0 = No, 1 = Yes | 범주형, 확인 결과 데이터 타입이 결정됨. |
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형, 숫자로 표현되지만 수치값으로 해석되지 않고 등급을 나타내기 때문 |
| sex | Sex | male, female | 범주형, 성별을 나타내기 위한 카테고리로서, 숫자로 표현되지 않고 문자열로서 의미를 갖기 때문에 범주형 데이터 타입 |
| Age | Age in years | 22.0, 38.0, 26.0, 35.0, ... | 수치형, 연령을 숫자로 나타내므로, 범주형이 아닌 수치형 데이터 타입 |
| sibsp | # of siblings / spouses aboard the Titanic | 1, 1, 0, 1, 0, ... | 숫자형, 형제자매/배우자의 수를 정수 값으로 나타내므로, 범주형이 아닌 수치형 데이터 타입 |
| parch | # of parents / children aboard the Titanic | 0, 0, 0, 0, 0, ... | 숫자형, 부모/자녀의 수를 정수 값으로 나타내므로, 범주형이 아닌 수치형 데이터 타입 |
| ticket | Ticket number | A/5 21171, PC 17599, STON/O2. 3101282, ... | 범주형, 문자열 데이터는 범주형 데이터 타입에 해당함 |
| fare | Passenger fare | 7.2500, 71.2833, 7.9250, ... | 수치형, 지불한 요금을 나타내기 위한 숫자이므로, 수치형 데이터 타입 |
| cabin | Cabin number | NaN, C85, NaN, C123, ... | 범주형, 객실 번호를 나타내기 위한 문자열이므로, 범주형 데이터 타입 |
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton | 범주형, 승객이 탑승한 항구를 나타내기 위한 문자열이므로, 범주형 데이터 타입 |

</details>

<details>
<summary>TypeOfContractChannel</summary>

#### DDA
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | --- |
| id | id | | 범주형의 명목형, 데이터를 식별하거나 구분하기 위한 고유한 식별자이기 때문 |
| type_of_contract | membership | 렌탈, 멤버십 | 범주형의 명목형, 계약의 다양한 유형을 명목적으로 나타내기 때문 |
| type_of_contract2	 | Package | Normal, TAS ... | 범주형의 명목형, 데이터 간의 순서나 계층을 나타내지 않기 때문 |
| channel | How | 서비스 방문, 홈쇼핑/방송 ... | 범주형의 명목형, 범주형의 명목형, 계약의 다양한 유형을 명목적으로 나타내기 때문 |
| datetime | datetime | | 범주형의 순서형, 시간적인 순서를 나타내기 때문 |
| Term | Term | 60, 12 ... |  |
| payment_type | payment_type | CMS, 카드이체 ... | 수치형의 이산형, 대기 시간이 정수로 표현되고 있음 |
| product | product | K1, K2, K3 ... | 범주형의 명목형, 제품이 서로 다른 값들 간에 순서가 있기 때문 |
| amount | amount | | 수치형의 연속형, 숫자 간에 연산이 가능하고 등간성이 있음 |
| state | state | 계약확정, 해약확정 | 범주형의 명목형, 각각 서로 다른 범주를 나타냄 |
| overdue_count | overdue_count | 0, 1 | 수치형의 이산형, 연속성은 없고 서로 다른 이산적인 값을 가지며 각 값이 서로 중복되지 않음 |
| overdue | overdue | 없음, 있음 | 범주형의 명목형, 확인 결과 데이터 타입이 결정됨 |
| credit rating | credit rating | 9, 2, 8 ... | 범주형의 순서형, 순서 관계를 가지기 때문 |
| bank | where | 새마을금고, 현대카드, 우리은행 ... | 범주형의 명목형 |
| cancellation | cancellation | 정상, 해약 | 범주형의 명목형 |
| age | age in years | | 수치형의 이산형, 연령을 숫자로 나타내므로, 범주형이 아닌 수치형 데이터 타입 |
| Mileage | Mileage | | 수치형의 이산형 |

</details>