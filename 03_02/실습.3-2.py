# 배열의 스캔을 for 문으로 구현하면 코드가 더 짧고 간결해진다.
# 실슬 3-1에서 작성한 while 문을 for문으로 수정하면 이렇게 나타낸다.

from typing import Any, Sequence

def seq_search(a:Sequence, key:Any) -> int: