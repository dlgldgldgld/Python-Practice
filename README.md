TOC
- [Python-Practice](#python-practice)
  * [01-LazyProperty.py](#01-lazypropertypy)
  * [02-ThreadPoolExecutor-example.py](#02-threadpoolexecutor-examplepy)
  * [03-Abnormal-Thread-Example.py](#03-abnormal-thread-examplepy)
  * [04-ProcessPoolExecutor-example.py](#04-processpoolexecutor-examplepy)
  * [05-Selenuim-ProcessToolExecutor.py](#05-selenuim-processtoolexecutorpy)
  * [06-async-coroutine.py](#06-async-coroutinepy)
  * [07-unit-test](#07-unit-test)
- [Numpy](#numpy)
  * [Numpy 사용 이유](#numpy------)
- [Python package 관련 정리](#python-package------)
  * [01. pip-command](#01-pip-command)
  * [02. 패키지 작성](#02-------)
- [argparse](#argparse)
  * [1. 기본 사용 코드 예제](#1------------)
  * [2. parse_args(args=None, namespace=None) method](#2-parse-args-args-none--namespace-none--method)
  * [3. add_argument](#3-add-argument)



# Python-Practice
Python 구문 정리용

[ Reference ]
- 효율적 개발로 이끄는 알고리즘 ( https://github.com/Jpub/fulfillPython ) 

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

## 05-Selenuim-ProcessToolExecutor.py
- ProcessToolExecutor를 Selenium으로 실행.

## 06-async-coroutine.py
- asyncio, coroutine 예제

## 07-unit-test
- 구현 방법
  1. test로 시작하는 이름으로 테스트 모듈을 생성
  2. unittest.TestCase 클래스의 서브클래스를 작성
  3. 내부에는 test로 시작하는 이름으로 테스트 메서드 구현.
  4. assert를 통해 결과값 체크 가능.
     1. assertEqual, asserTrue, asserIsNone, assertIn, assertAlmostEqual 등 지원.
  5. 전처리 후처리는 setup(), tearDown() function을 구현하면 됨.
- test 결과 확인 방법
  - python -m unittest -v : 항목으로 test 가능.
    - 특정 test만 하려면 뒤에 패키지-모듈-클래스 순으로 입력 
      - ex1 ) `python -m unittest -v test.test_api.BuildUrl.test_build_url`
      - ex2 ) `python -m unittest -v test.test_api.BuildUrl`
      - ex3 ) `python -m unittest -v test.test_api`
    - pattern 형식으로 적용하려면 아래의 코드 수행
      - `python -m unittest discover -s test -p test_c*.py -v` : test 모듈의 test_c*.py 패턴만 수행함.
  - @unittest.expectedFailure : 실패하는 test는 이 decorator를 추가하면 pass 가능.
- 더 자세한 내용은 [https://docs.python.org/3/library/unittest.html#organizing-test-code](https://docs.python.org/3/library/unittest.html#organizing-test-code) 참조

# Numpy
## Numpy 사용 이유
- Python Array는 메모리 사용이 효율적이지 못하다.
- Numypt는 multi dementions 변수를 다룰때 빠른 속도를 위해 사용한다.

# Python package 관련 정리
## 01. pip-command
- pip install --upgarde pip : package update
- pip install -r requirements.lcok : requirements.lock에 있는 package를 현재 python 환경에 설치
- pip freeze > requirements.lock : 현재 package 설치 목록을 requirements.lock 에 저장

## 02. 패키지 작성
- No plan


# argparse
## 1. 기본 사용 코드 예제
```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.') # 1. ArgumentParser 생성
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator') # 2. add_argument 함수를 통해 argument  추가.
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args() # 3. 인자를 받아옴.
print(args.accumulate(args.integers)) # 4. 인자값 사용
```

## 2. parse_args(args=None, namespace=None) method
- 인자 설명
  - args - List of strings to parse. The default is taken from **sys.argv**.
  - namespace - An object to take the attributes. The default is a new empty Namespace object.

- cli를 검사하고 올바른 값으로 인자를 convert 해주는 함수이다.
  ```python
  args = parser.parse_args()
  args.target
  args.env
  ```
- 인자로 넘기는 값이 유효한지 체크할때도 사용이 가능하다.
  ```python
  parser.add_argument('--foo')
  parser.parse_args(['spam']) # error occur.
  ```
- **리스트로 감싸서 사용해야 함.**

## 3. add_argument
- doc : https://docs.python.org/3/library/argparse.html#the-add-argument-method
- positional argument : 무조건 들어가야하는 argument를 뜻함.
  - 예를 들어 아래의 코드에서는 무조건 인자값이 포함되어야 함.
    ```python
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_arguments('bar'. type=int)
    ```
    > python example.py 1 <- 1이 bar 자리가 됨.
- optional argument : 들어가도되고, 안들어가도 되는 argument, 선언시 앞에 `-`을 붙인다.
- action : cli argument에 action을 부여한다는 뜻으로, default로는 `store`가 부여된다. add_arguement에 keyword argument로 부여가 가능하다.
  - store : argument에 값을 저장하겠다는 의미. ex) --foo 1 > Namespace(foo = '1')
  - store_const : const 옵션으로 값을 지정해주겠다는 의미이다. 예를 들어 `--foo` 라고 argument를 넣어주기만 한다면 const의 값을 넣어주겠다는 뜻.
    ``` python
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store_const', const=42)
    parser.parse_args(['--foo'])
    >>> Namespace(foo=42)
    parser.parse_args(['--foo', '1'])
    >>> 지정하는 argument라고 에러가 발생함.
    ```
 - store_true, store_false : argument 설정시 true나 false를 저장하는 action. args를 전달하지 않는다면 false나 true가 설정된다.
 - append : list 형식으로 값을 append하는 action.
   ```python
   parser.add_argument('--foo', action='append')
   parser.parse_args('--foo 1 --foo 2'.split())
   >> Namespace(foo=['1', '2'])
   ```
 - version : 흔히 library에 --version을 입력할때 나오는 구문과 동일하다고 생각하면 됨. 아래와 같이 사용 가능함.
    ``` python
    import argparse
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('--version', action='version', version='%(prog)s 2.0')
    parser.parse_args(['--version'])
    >> PROG 2.0
    ```

## 4. itertools 
- iterator를 사용할때 itertools를 쓰면 이터레이터간 연결, filter, 조합등을 쉽게 할 수 있다.