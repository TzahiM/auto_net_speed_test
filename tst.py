# -*- coding: utf-8 -*-
import sys
import pyspeedtest
import time


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

'''
Read the following parameters:

'''
def calc_min_max( min_val, max_val, current_value):
    max = max_val
    min = min_val
    if current_value > max_val:
        max = current_value
    if current_value < min_val:
        min = current_value
    return min , max



def speed_test( number_of_iterations = 1, interval_minutes = 0 ):
    print 'starting ' + str(number_of_iterations) + ' iterations at ' + str(interval_minutes) + ' minutes interval'
    st = pyspeedtest.SpeedTest()
    dnl_max = 0
    dnl_min = 1000
    upl_max = 0
    upl_min = 1000
    ping_max = 0
    ping_min = 1000000
    
    for iterations in range(number_of_iterations):
        ping_msec = st.ping()
        dnl_mega = st.download() / 1000000
        upl_mega   = st.upload()   / 1000000
        ping_min, ping_max = calc_min_max( ping_min, ping_max, ping_msec)
        dnl_min, dnl_max = calc_min_max( dnl_min, dnl_max, dnl_mega)
        upl_min, upl_max = calc_min_max( upl_min, upl_max, upl_mega)

        min_max_string =  ' ping min ' + str(ping_min) + ' ping_max ' + str(ping_max) + ' dnl_min ' + str( dnl_min) + ' dnl_max ' + str( dnl_max) +  ' upl_min ' + str( upl_min) + ' upl_max ' + str( upl_max)
        print  iterations ,'ping msec ' , ping_msec , 'dnl mega' , dnl_mega , 'upl mega' , upl_mega, min_max_string
        time.sleep(interval_minutes * 60)

def run_test():
    n_args = len(sys.argv)
    if n_args is 1:
        speed_test()
        return
    if n_args is 2:
        speed_test( number_of_iterations = int(sys.argv[1]))
        return
    speed_test( number_of_iterations = int(sys.argv[1]), interval_minutes = int(sys.argv[2]))



run_test()






 