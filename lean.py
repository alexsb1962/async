# -*- coding: utf8 -*-

import time
#import sys

class frange():
    def __init__(self,start:float,end:float,dx:float=1.0,eps:float=sys.float_info.epsilon):
        if dx == 0.0:
            raise StopIteration
        else:
            if dx < 0:
                self.xe = min(start,end)
                self.xs = max(start,end)
            else:
                self.xs = min(start,end)
                self.xe = max(start,end)

            self.xd =dx
            self.x=self.xs

    def __iter__(self):
        return(self)

    def __next__(self):
        result=self.x
        self.x+=self.xd
        if self.xd>0:
            if result>self.xe:
                raise StopIteration
        else:
            if result<self.xe:
                raise StopIteration
        return(result)



def main():
    l=[]
    print(list(l for l in frange(1.0,5.0,0.5)))
    print(list(l for l in frange(5.0,1.0,0.5)))
    print(list(l for l in frange(-1.0,-5.0,0.5)))
    print(list(l for l in frange(-5.0,-1.0,-0.5)))


if __name__=="__main__":
    main()
