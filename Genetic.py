class Genes():
    def __init__(self,status):#생성자 초기화
        self.status = status
        self.similar = 0
        self.what_similar()

    def what_similar(self):
        '''
            111111 6자리 최종유전자.
        '''
        for i in str(self.status):#status 6자리 랜덤숫자
            if i == '1':
                self.similar += 1                
    
    def __del__(self):#소멸자
        print(self.status, '사망')