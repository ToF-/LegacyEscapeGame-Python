#!/usr/bin/env python3
import sys
import os
import csv
import time
from datetime import datetime

class Order:
    def __init__(self, id, start, duration, price):
        self.id = id
        self.start = start
        self.duration = duration
        self.price = price

def rev(orders):
    if len(orders) == 0:
        return 0
    order = orders[0]
    start = order.start
    end = start + order.duration
    year = start // 1000
    year_end = year * 1000 + 365
    if end > year_end:
        days = end - year_end
        end = (year + 1) * 1000 + days
    l = []
    for o in orders:
        if o.start >= end:
            l.append(o)
    l2 = []
    for i in range(1,len(orders)):
        l2.append(orders[i])
    r = order.price + rev(l)
    r2 = rev(l2)
    return(max(r, r2))

def main(argv):
    data_file = os.getenv("LAGS_ORDER_FILE");
    tot = 0
    with open(data_file,'r') as f:
        orderList = []
        csv_reader = csv.reader(f)
        for line_no, line in enumerate(csv_reader,0):
            if line_no > 0:
                field1 = line[0]
                fld2 = int(line[1])
                field3 = int(line[2])
                fld4 = int(line[3])
                order = Order(field1, fld2, field3, fld4)
                orderList.append(order)
    orderList.sort(key = lambda order: order.start)
    for i in range(0, len(orderList)-1):
        assert orderList[i].start <= orderList[i+1].start, "list should be ordered"
        tot+= 1
    rv = rev(orderList)
    fmt = "{:d} {:d}"
    print(fmt.format(tot+1,rv))
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])

