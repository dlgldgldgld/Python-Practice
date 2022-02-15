# Python-Practice
Python 구문 정리용

## 01-LazyProperty.py
- LazyProperty : 최초에 한번 수행된 이후에는 다시 계산을 하지 않는 Class Property

## 02-ThreadPoolExecutor-example.py
- ThreadPoolExecutor에 대해서 알아보자.

## 03-Abnormal-Thread-Example.py
- 잘못 사용 된 ThreadPoolExecutor 사용 케이스에 대해서 알아봄. ( lock 옵션 부재 )

## 04-ProcessPoolExecutor-example.py
- ProcessPoolExecutor를 이용한 멀티프로세싱 구현
- 순차구현, Thread, MultiProcess 환경에서 fibonaci 함수 실행.
  - 수행 속도 : Thread > 순차구현 > MultiProcess