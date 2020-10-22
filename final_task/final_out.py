#!/usr/bin/env python
from final_task import Matrix
from final_task import HorizontalVector
from final_task import VerticalVector

if __name__ == '__main__':
    psm = Matrix( [1, 2, 3, 4, 5, 6],3,2 )    # 3x2 from list
    psm.draw()
    asm = Matrix( [[7, 2, 3], [4, 5, 6]] )    # 2x3 from array
    asm.draw()
    print('Multi')
    rsm=psm*asm
    rsm.draw()
    print('identity -',rsm.is_identity())
    print('square -', rsm.is_square())
    print('zero -', rsm.is_zero())
    print('diagonal -',rsm.is_diagonal())
    print('')

    am = Matrix([],3,3)                       # 3x3 random
    am.draw()
    am.transpose()
    print('Trunspouse')
    am.draw()
    print('identity -',am.is_identity())
    print('square -', am.is_square())
    print('zero -',am.is_zero())
    print('diagonal -',am.is_diagonal())
    print('')

    pm = Matrix( [1,0,0,0,1,0,0,0,1],3,3 )    # 3x3 identity
    pm.draw()
    print('identity -',pm.is_identity())
    print('square -', pm.is_square())
    print('zero -',pm.is_zero())
    print('diagonal -',pm.is_diagonal())
    print('')
    print('Sum')
    rm=am+pm
    rm.draw()
    print('Sub')
    sm=am-pm
    sm.draw()



    hv = HorizontalVector([1,2,3,4,5])
    hv.draw()
    vv = VerticalVector([],6)
    vv.draw()
    vm=vv*hv
    vm.draw()

    
    im = Matrix(psm.matr)
    print(str(im))
    im.draw()
    