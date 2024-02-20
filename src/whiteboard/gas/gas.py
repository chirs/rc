# https://www.interviewbit.com/problems/gas-station/

def find_start(costl, gasl):
    # Basically, you're looking for the last time that the gas tank slips below 0.

    netl = [a-b for a,b in zip(gasl, costl)]

    if sum(netl) < 0:
        return -1
    else:
        tank = 0
        start_index = 0
        for index, net_gas in netl:
            tank += net_gas
            if tank < 0:
                start_index = index+1
        return start_index



        
