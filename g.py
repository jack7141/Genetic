from echo import Ecosystem as ec
from random import random

if __name__ == '__main__':
    print(0, '번째')
    echo = ec(0)
    for i in echo.gene_list:
        if i is not None:
            print(i.status, i.similar)

    #부모유전자선택에서 for문을 2번 돌렸기 때문에 2가지만 뽑아낸다.
    print('0세대 상위 유전자')
    print(echo.parents[0].status, echo.parents[0].similar)
    print(echo.parents[1].status, echo.parents[1].similar)
    print('==========================')
    
