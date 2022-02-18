from unittest.mock import Mock

# return_value를 통해 mock을 생성할 수 있음.
# 인수를 넣어도 그대로임.
mock = Mock(return_value=3)
mock.return_value = 4

mock(1) # 4
mock() # 4

# 더 세세하게 동작을 제어하고 싶을때는 side_effect 인수를 넣음.
mock = Mock(side_effect=lambda x : x + 2)
print(mock(5))

mock.side_effect = [2,1]
print(mock())
print(mock())

## Error 값도 넣을 수 있음. 
# mock.side_effect = ValueError('error')
# print(mock())

# 호출 여부 확인
## - assert_not_called() 호출한적이 있다면 에러 발생.
## - assert_called_once() 한번도 호출하지 않으면 에러 발생. 2번이상 호출해도 에러 발생.
mock = Mock(return_value = 3)

mock.assert_not_called()
mock()
mock.assert_called_once()

## 어떤 인수를 사용해서 호출했는지도 확인이 가능하다.
mock = Mock(return_value = 3)
mock(1, a=2)
mock.assert_called_once_with(1, a=2)


# ANY 를 통해서도 확인이 가능함.
mock(2, a=4)
from unittest.mock import ANY
mock.assert_called_with(2, a=ANY)

