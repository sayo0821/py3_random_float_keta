# -*- coding: utf8 -*-

import random


def myfn_001(flt1,flt2,intKeta):
    # 範囲と小数点桁数を指定して乱数を返す関数

    # 「random.uniform(a,b)」は、任意の範囲の浮動小数点を返す
    # print(random.uniform(100, 200))
    # 175.26585048238275
    ret = None    # 戻り値を初期化
    ret = random.uniform(flt1,flt2)

    # format関数を使用して桁数を指定する方法
    # 「"{:.3f}".format(number)」
    strKeta = "{:." + str(intKeta) + "f}"
    ret = strKeta.format(ret)

    return ret


print(myfn_001(10,30,1))    # --> 13.5
