"""
written by Jannik Czinzoll
Labor Vout Difference
15,5	3,314	4,677127339
14,6	3,129	4,666027485
14	2,995	4,674457429
13,5	2,887	4,676134396
13	2,781	4,67457749
12,5	2,676	4,671150972
12	2,569	4,671078241
11,5	2,455	4,684317719
11	2,356	4,66893039
10,5	2,239	4,689593569
10	2,153	4,644681839
9,5	2,033	4,672897196
9	1,927	4,670472237
8,5	1,824	4,660087719
8	1,723	4,643064423
7,5	1,626	4,612546125
7	1,509	4,638833665
6,5	1,404	4,62962963
6	1,29	4,651162791

	Durchschnitt	4,661935298
		4,66V
"""

from machine import Pin, ADC

VOLTAGE_FACTOR: float = 4.66
voltage_sensor_pin : int = 0

def battery_voltage():
    pin_value = voltage_sensor_pin.read_u16()
    voltage = pin_value * (3.3/65535) * VOLTAGE_FACTOR
    return voltage