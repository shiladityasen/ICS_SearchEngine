import sys
sys.path.insert(0, '../MongoCodes')

from VitalConstants import *

INVHEADCOLL = INVIDXCOLL + '_head'
INVBODYCOLL = INVIDXCOLL + '_body'
INVANCHORCOLL = INVIDXCOLL + '_anchor'

HEAD_WT = 1.0
BODY_WT = 0.65
ANCHOR_WT = 1.25

NET_WT = HEAD_WT+BODY_WT+ANCHOR_WT
HEAD_WT /= NET_WT
BODY_WT /= NET_WT
ANCHOR_WT /= NET_WT

GOOGLE_RESULTS_DELIM = '`````'