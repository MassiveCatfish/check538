from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import requests

from .models import Greeting

import math
import random
import json
from pprint import pprint
#import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from time import mktime

import os

pollHistory = []
kitchenHistory = []
PWHistory = []

#read and load all files from 538
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
AL_D_json=open(os.path.join(SITE_ROOT, "static", "AL_D.json")).read()
AL_R_json=open(os.path.join(SITE_ROOT, "static", "AL_R.json")).read()
AR_D_json=open(os.path.join(SITE_ROOT, "static", "AR_D.json")).read()
AR_R_json=open(os.path.join(SITE_ROOT, "static", "AR_R.json")).read()
AZ_D_json=open(os.path.join(SITE_ROOT, "static", "AZ_D.json")).read()
AZ_R_json=open(os.path.join(SITE_ROOT, "static", "AZ_R.json")).read()
CA_D_json=open(os.path.join(SITE_ROOT, "static", "CA_D.json")).read()
CA_R_json=open(os.path.join(SITE_ROOT, "static", "CA_R.json")).read()
CT_D_json=open(os.path.join(SITE_ROOT, "static", "CT_D.json")).read()
CT_R_json=open(os.path.join(SITE_ROOT, "static", "CT_R.json")).read()
FL_D_json=open(os.path.join(SITE_ROOT, "static", "FL_D.json")).read()
FL_R_json=open(os.path.join(SITE_ROOT, "static", "FL_R.json")).read()
GA_D_json=open(os.path.join(SITE_ROOT, "static", "GA_D.json")).read()
GA_R_json=open(os.path.join(SITE_ROOT, "static", "GA_R.json")).read()
IA_D_json=open(os.path.join(SITE_ROOT, "static", "IA_D.json")).read()
IA_R_json=open(os.path.join(SITE_ROOT, "static", "IA_R.json")).read()
IL_D_json=open(os.path.join(SITE_ROOT, "static", "IL_D.json")).read()
IL_R_json=open(os.path.join(SITE_ROOT, "static", "IL_R.json")).read()
IN_D_json=open(os.path.join(SITE_ROOT, "static", "IN_D.json")).read()
IN_R_json=open(os.path.join(SITE_ROOT, "static", "IN_R.json")).read()
KS_R_json=open(os.path.join(SITE_ROOT, "static", "KS_R.json")).read()
LA_D_json=open(os.path.join(SITE_ROOT, "static", "LA_D.json")).read()
LA_R_json=open(os.path.join(SITE_ROOT, "static", "LA_R.json")).read()
MA_D_json=open(os.path.join(SITE_ROOT, "static", "MA_D.json")).read()
MA_R_json=open(os.path.join(SITE_ROOT, "static", "MA_R.json")).read()
MD_D_json=open(os.path.join(SITE_ROOT, "static", "MD_D.json")).read()
MD_R_json=open(os.path.join(SITE_ROOT, "static", "MD_R.json")).read()
MI_D_json=open(os.path.join(SITE_ROOT, "static", "MI_D.json")).read()
MI_R_json=open(os.path.join(SITE_ROOT, "static", "MI_R.json")).read()
MO_D_json=open(os.path.join(SITE_ROOT, "static", "MO_D.json")).read()
MO_R_json=open(os.path.join(SITE_ROOT, "static", "MO_R.json")).read()
MS_D_json=open(os.path.join(SITE_ROOT, "static", "MS_D.json")).read()
NC_D_json=open(os.path.join(SITE_ROOT, "static", "NC_D.json")).read()
NC_R_json=open(os.path.join(SITE_ROOT, "static", "NC_R.json")).read()
NH_D_json=open(os.path.join(SITE_ROOT, "static", "NH_D.json")).read()
NH_R_json=open(os.path.join(SITE_ROOT, "static", "NH_R.json")).read()
NJ_D_json=open(os.path.join(SITE_ROOT, "static", "NJ_D.json")).read()
NJ_R_json=open(os.path.join(SITE_ROOT, "static", "NJ_R.json")).read()
NV_D_json=open(os.path.join(SITE_ROOT, "static", "NV_D.json")).read()
NV_R_json=open(os.path.join(SITE_ROOT, "static", "NV_R.json")).read()
NY_D_json=open(os.path.join(SITE_ROOT, "static", "NY_D.json")).read()
NY_R_json=open(os.path.join(SITE_ROOT, "static", "NY_R.json")).read()
OH_D_json=open(os.path.join(SITE_ROOT, "static", "OH_D.json")).read()
OH_R_json=open(os.path.join(SITE_ROOT, "static", "OH_R.json")).read()
OK_D_json=open(os.path.join(SITE_ROOT, "static", "OK_D.json")).read()
OK_R_json=open(os.path.join(SITE_ROOT, "static", "OK_R.json")).read()
PA_D_json=open(os.path.join(SITE_ROOT, "static", "PA_D.json")).read()
PA_R_json=open(os.path.join(SITE_ROOT, "static", "PA_R.json")).read()
RI_D_json=open(os.path.join(SITE_ROOT, "static", "RI_D.json")).read()
RI_R_json=open(os.path.join(SITE_ROOT, "static", "RI_R.json")).read()
SC_D_json=open(os.path.join(SITE_ROOT, "static", "SC_D.json")).read()
SC_R_json=open(os.path.join(SITE_ROOT, "static", "SC_R.json")).read()
TN_D_json=open(os.path.join(SITE_ROOT, "static", "TN_D.json")).read()
TN_R_json=open(os.path.join(SITE_ROOT, "static", "TN_R.json")).read()
TX_D_json=open(os.path.join(SITE_ROOT, "static", "TX_D.json")).read()
TX_R_json=open(os.path.join(SITE_ROOT, "static", "TX_R.json")).read()
UT_D_json=open(os.path.join(SITE_ROOT, "static", "UT_D.json")).read()
UT_R_json=open(os.path.join(SITE_ROOT, "static", "UT_R.json")).read()
VA_D_json=open(os.path.join(SITE_ROOT, "static", "VA_D.json")).read()
VA_R_json=open(os.path.join(SITE_ROOT, "static", "VA_R.json")).read()
VT_D_json=open(os.path.join(SITE_ROOT, "static", "VT_D.json")).read()
WI_D_json=open(os.path.join(SITE_ROOT, "static", "WI_D.json")).read()
WI_R_json=open(os.path.join(SITE_ROOT, "static", "WI_R.json")).read()
WV_D_json=open(os.path.join(SITE_ROOT, "static", "WV_D.json")).read()
WV_R_json=open(os.path.join(SITE_ROOT, "static", "WV_R.json")).read()


AL_D_data = json.loads(AL_D_json)
AL_R_data = json.loads(AL_R_json)
AR_D_data = json.loads(AR_D_json)
AR_R_data = json.loads(AR_R_json)
AZ_D_data = json.loads(AZ_D_json)
AZ_R_data = json.loads(AZ_R_json)
CA_D_data = json.loads(CA_D_json)
CA_R_data = json.loads(CA_R_json)
CT_D_data = json.loads(CT_D_json)
CT_R_data = json.loads(CT_R_json)
FL_D_data = json.loads(FL_D_json)
FL_R_data = json.loads(FL_R_json)
GA_D_data = json.loads(GA_D_json)
GA_R_data = json.loads(GA_R_json)
IA_D_data = json.loads(IA_D_json)
IA_R_data = json.loads(IA_R_json)
IL_D_data = json.loads(IL_D_json)
IL_R_data = json.loads(IL_R_json)
IN_D_data = json.loads(IN_D_json)
IN_R_data = json.loads(IN_R_json)
KS_R_data = json.loads(KS_R_json)
LA_D_data = json.loads(LA_D_json)
LA_R_data = json.loads(LA_R_json)
MA_D_data = json.loads(MA_D_json)
MA_R_data = json.loads(MA_R_json)
MD_D_data = json.loads(MD_D_json)
MD_R_data = json.loads(MD_R_json)
MI_D_data = json.loads(MI_D_json)
MI_R_data = json.loads(MI_R_json)
MO_D_data = json.loads(MO_D_json)
MO_R_data = json.loads(MO_R_json)
MS_D_data = json.loads(MS_D_json)
NC_D_data = json.loads(NC_D_json)
NC_R_data = json.loads(NC_R_json)
NH_D_data = json.loads(NH_D_json)
NH_R_data = json.loads(NH_R_json)
NJ_D_data = json.loads(NJ_D_json)
NJ_R_data = json.loads(NJ_R_json)
NV_D_data = json.loads(NV_D_json)
NV_R_data = json.loads(NV_R_json)
NY_D_data = json.loads(NY_D_json)
NY_R_data = json.loads(NY_R_json)
OH_D_data = json.loads(OH_D_json)
OH_R_data = json.loads(OH_R_json)
OK_D_data = json.loads(OK_D_json)
OK_R_data = json.loads(OK_R_json)
PA_D_data = json.loads(PA_D_json)
PA_R_data = json.loads(PA_R_json)
RI_D_data = json.loads(RI_D_json)
RI_R_data = json.loads(RI_R_json)
SC_D_data = json.loads(SC_D_json)
SC_R_data = json.loads(SC_R_json)
TN_D_data = json.loads(TN_D_json)
TN_R_data = json.loads(TN_R_json)
TX_D_data = json.loads(TX_D_json)
TX_R_data = json.loads(TX_R_json)
UT_D_data = json.loads(UT_D_json)
UT_R_data = json.loads(UT_R_json)
VA_D_data = json.loads(VA_D_json)
VA_R_data = json.loads(VA_R_json)
VT_D_data = json.loads(VT_D_json)
WI_D_data = json.loads(WI_D_json)
WI_R_data = json.loads(WI_R_json)
WV_D_data = json.loads(WV_D_json)
WV_R_data = json.loads(WV_R_json)


################################
#read and load all data from PW

IA_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1533.json")).read()
NH_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1534.json")).read()
SC_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1553.json")).read()
NV_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1554.json")).read()
AL_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1571.json")).read()
AK_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1572.json")).read()
GA_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1575.json")).read()
AR_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1573.json")).read()
MA_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1576.json")).read()
MN_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1577.json")).read()
OK_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1578.json")).read()
TN_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1579.json")).read()
TX_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1580.json")).read()
VA_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1582.json")).read()
KS_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1642.json")).read()
KY_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1638.json")).read()
LA_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1639.json")).read()
ME_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1640.json")).read()
PR_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1641.json")).read()
HI_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1650.json")).read()
ID_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1651.json")).read()
MI_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1652.json")).read()
MS_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1653.json")).read()
DC_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1670.json")).read()
FL_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1661.json")).read()
IL_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1660.json")).read()
MO_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1662.json")).read()
NC_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1663.json")).read()
OH_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1659.json")).read()
AZ_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1672.json")).read()
UT_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1673.json")).read()


IA_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1541.json")).read()
NH_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1540.json")).read()
NV_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1606.json")).read()
SC_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1607.json")).read()
AL_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1614.json")).read()
AR_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1615.json")).read()
CO_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1616.json")).read()
GA_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1617.json")).read()
MA_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1618.json")).read()
MN_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1619.json")).read()
OK_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1620.json")).read()
TN_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1621.json")).read()
TX_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1622.json")).read()
VT_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1623.json")).read()
VA_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1624.json")).read()
KS_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1643.json")).read()
LA_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1644.json")).read()
NE_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1645.json")).read()
ME_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1646.json")).read()
MI_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1649.json")).read()
MS_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1648.json")).read()
FL_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1654.json")).read()
IL_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1655.json")).read()
MO_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1656.json")).read()
NC_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1657.json")).read()
OH_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1658.json")).read()
AZ_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1679.json")).read()
UT_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1678.json")).read()
ID_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1681.json")).read()
AK_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1686.json")).read()
HI_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1687.json")).read()
WA_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1688.json")).read()
WI_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1703.json")).read()
WI_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1695.json")).read()
WY_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1696.json")).read()
NY_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1704.json")).read()
NY_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1697.json")).read()




CT_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1705.json")).read()
DE_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1706.json")).read()
MD_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1707.json")).read()
PA_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1708.json")).read()
RI_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1709.json")).read()
CT_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1698.json")).read()
DE_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1699.json")).read()
MD_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1700.json")).read()
PA_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1701.json")).read()
RI_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1702.json")).read()
IN_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1721.json")).read()
NE_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1722.json")).read()
WV_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1723.json")).read()
IN_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1726.json")).read()
WV_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1727.json")).read()
KY_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1728.json")).read()
OR_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1729.json")).read()
OR_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1724.json")).read()
WA_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1725.json")).read()
CA_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1741.json")).read()
MT_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1742.json")).read()
NJ_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1743.json")).read()
NM_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1744.json")).read()
SD_Rp_json=open(os.path.join(SITE_ROOT, "static", "table_1745.json")).read()
CA_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1746.json")).read()
MT_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1751.json")).read()
NJ_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1749.json")).read()
NM_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1752.json")).read()
ND_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1750.json")).read()
SD_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1748.json")).read()
DC_Dp_json=open(os.path.join(SITE_ROOT, "static", "table_1753.json")).read()

##################################

IA_Rp_data = json.loads(IA_Rp_json)
NH_Rp_data = json.loads(NH_Rp_json)
SC_Rp_data = json.loads(SC_Rp_json)
NV_Rp_data = json.loads(NV_Rp_json)
AL_Rp_data = json.loads(AL_Rp_json)
AK_Rp_data = json.loads(AK_Rp_json)
AR_Rp_data = json.loads(AR_Rp_json)
GA_Rp_data = json.loads(GA_Rp_json)
MA_Rp_data = json.loads(MA_Rp_json)
MN_Rp_data = json.loads(MN_Rp_json)
OK_Rp_data = json.loads(OK_Rp_json)
TN_Rp_data = json.loads(TN_Rp_json)
TX_Rp_data = json.loads(TX_Rp_json)
VA_Rp_data = json.loads(VA_Rp_json)
KS_Rp_data = json.loads(KS_Rp_json)
KY_Rp_data = json.loads(KY_Rp_json)
LA_Rp_data = json.loads(LA_Rp_json)
ME_Rp_data = json.loads(ME_Rp_json)
PR_Rp_data = json.loads(PR_Rp_json)
HI_Rp_data = json.loads(HI_Rp_json)
ID_Rp_data = json.loads(ID_Rp_json)
MI_Rp_data = json.loads(MI_Rp_json)
MS_Rp_data = json.loads(MS_Rp_json)
DC_Rp_data = json.loads(DC_Rp_json)
FL_Rp_data = json.loads(FL_Rp_json)
IL_Rp_data = json.loads(IL_Rp_json)
MO_Rp_data = json.loads(MO_Rp_json)
NC_Rp_data = json.loads(NC_Rp_json)
OH_Rp_data = json.loads(OH_Rp_json)
AZ_Rp_data = json.loads(AZ_Rp_json)
UT_Rp_data = json.loads(UT_Rp_json)



IA_Dp_data = json.loads(IA_Dp_json)
NH_Dp_data = json.loads(NH_Dp_json)
NV_Dp_data = json.loads(NV_Dp_json)
SC_Dp_data = json.loads(SC_Dp_json)
AL_Dp_data = json.loads(AL_Dp_json)
AR_Dp_data = json.loads(AR_Dp_json)
CO_Dp_data = json.loads(CO_Dp_json)
GA_Dp_data = json.loads(GA_Dp_json)
MA_Dp_data = json.loads(MA_Dp_json)
MN_Dp_data = json.loads(MN_Dp_json)
OK_Dp_data = json.loads(OK_Dp_json)
TN_Dp_data = json.loads(TN_Dp_json)
TX_Dp_data = json.loads(TX_Dp_json)
VT_Dp_data = json.loads(VT_Dp_json)
VA_Dp_data = json.loads(VA_Dp_json)
KS_Dp_data = json.loads(KS_Dp_json)
LA_Dp_data = json.loads(LA_Dp_json)
NE_Dp_data = json.loads(NE_Dp_json)
ME_Dp_data = json.loads(ME_Dp_json)
MI_Dp_data = json.loads(MI_Dp_json)
MS_Dp_data = json.loads(MS_Dp_json)
FL_Dp_data = json.loads(FL_Dp_json)
IL_Dp_data = json.loads(IL_Dp_json)
MO_Dp_data = json.loads(MO_Dp_json)
NC_Dp_data = json.loads(NC_Dp_json)
OH_Dp_data = json.loads(OH_Dp_json)
AZ_Dp_data = json.loads(AZ_Dp_json)
UT_Dp_data = json.loads(UT_Dp_json)
ID_Dp_data = json.loads(ID_Dp_json)
AK_Dp_data = json.loads(AK_Dp_json)
HI_Dp_data = json.loads(HI_Dp_json)
WA_Dp_data = json.loads(WA_Dp_json)
WI_Rp_data = json.loads(WI_Rp_json)
WI_Dp_data = json.loads(WI_Dp_json)
WY_Dp_data = json.loads(WY_Dp_json)
NY_Rp_data = json.loads(NY_Rp_json)
NY_Dp_data = json.loads(NY_Dp_json)



CT_Rp_data = json.loads(CT_Rp_json)
DE_Rp_data = json.loads(DE_Rp_json)
MD_Rp_data = json.loads(MD_Rp_json)
PA_Rp_data = json.loads(PA_Rp_json)
RI_Rp_data = json.loads(RI_Rp_json)
CT_Dp_data = json.loads(CT_Dp_json)
DE_Dp_data = json.loads(DE_Dp_json)
MD_Dp_data = json.loads(MD_Dp_json)
PA_Dp_data = json.loads(PA_Dp_json)
RI_Dp_data = json.loads(RI_Dp_json)
IN_Rp_data = json.loads(IN_Rp_json)
NE_Rp_data = json.loads(NE_Rp_json)
WV_Rp_data = json.loads(WV_Rp_json)
IN_Dp_data = json.loads(IN_Dp_json)
WV_Dp_data = json.loads(WV_Dp_json)
KY_Dp_data = json.loads(KY_Dp_json)
OR_Dp_data = json.loads(OR_Dp_json)
OR_Rp_data = json.loads(OR_Rp_json)
WA_Rp_data = json.loads(WA_Rp_json)
CA_Rp_data = json.loads(CA_Rp_json)
MT_Rp_data = json.loads(MT_Rp_json)
NJ_Rp_data = json.loads(NJ_Rp_json)
NM_Rp_data = json.loads(NM_Rp_json)
SD_Rp_data = json.loads(SD_Rp_json)
CA_Dp_data = json.loads(CA_Dp_json)
MT_Dp_data = json.loads(MT_Dp_json)
NJ_Dp_data = json.loads(NJ_Dp_json)
NM_Dp_data = json.loads(NM_Dp_json)
ND_Dp_data = json.loads(ND_Dp_json)
SD_Dp_data = json.loads(SD_Dp_json)
DC_Dp_data = json.loads(DC_Dp_json)




# datalist of 538 results

dataList = [AL_D_data, AL_R_data, AR_D_data, AR_R_data, AZ_D_data, AZ_R_data, CA_D_data, CA_R_data, CT_D_data, CT_R_data, 
FL_D_data, FL_R_data, GA_D_data, GA_R_data, IA_D_data, IA_R_data, IL_D_data, IL_R_data, IN_D_data, IN_R_data, KS_R_data, 
LA_D_data, LA_R_data, MA_D_data, MA_R_data, MD_D_data, MD_R_data, MI_D_data, MI_R_data, MO_D_data, MO_R_data, MS_D_data, 
NC_D_data, NC_R_data, NH_D_data, NH_R_data, NJ_D_data, NJ_R_data, NV_D_data, NV_R_data, NY_D_data, NY_R_data, OH_D_data, 
OH_R_data, OK_D_data, OK_R_data, PA_D_data, PA_R_data, RI_D_data, RI_R_data, SC_D_data, SC_R_data, TN_D_data, TN_R_data, 
TX_D_data, TX_R_data, UT_D_data, UT_R_data, VA_D_data, VA_R_data, VT_D_data, WI_D_data, WI_R_data, WV_D_data, WV_R_data]

#data list of PW results
dataListp = [IA_Rp_data, NH_Rp_data, SC_Rp_data, NV_Rp_data, AL_Rp_data, AK_Rp_data, AR_Rp_data, GA_Rp_data, MA_Rp_data, 
MN_Rp_data, OK_Rp_data, TN_Rp_data, TX_Rp_data, VA_Rp_data, KS_Rp_data, KY_Rp_data, LA_Rp_data, ME_Rp_data, PR_Rp_data, 
HI_Rp_data, ID_Rp_data, MI_Rp_data, MS_Rp_data, DC_Rp_data, FL_Rp_data, IL_Rp_data, MO_Rp_data, NC_Rp_data, OH_Rp_data, 
AZ_Rp_data, UT_Rp_data, IA_Dp_data, NH_Dp_data, NV_Dp_data, SC_Dp_data, AL_Dp_data, AR_Dp_data, CO_Dp_data, GA_Dp_data, 
MA_Dp_data, MN_Dp_data, OK_Dp_data, TN_Dp_data, TX_Dp_data, VT_Dp_data, VA_Dp_data, KS_Dp_data, LA_Dp_data, NE_Dp_data, 
ME_Dp_data, MI_Dp_data, MS_Dp_data, FL_Dp_data, IL_Dp_data, MO_Dp_data, NC_Dp_data, OH_Dp_data, AZ_Dp_data, UT_Dp_data, 
ID_Dp_data, AK_Dp_data, HI_Dp_data, WA_Dp_data, WI_Rp_data, WI_Dp_data, WY_Dp_data, NY_Rp_data, NY_Dp_data, CT_Rp_data,
DE_Rp_data, MD_Rp_data, PA_Rp_data, RI_Rp_data, CT_Dp_data, DE_Dp_data, MD_Dp_data, PA_Dp_data, RI_Dp_data, IN_Rp_data,
NE_Rp_data, WV_Rp_data, IN_Dp_data, WV_Dp_data, KY_Dp_data, OR_Dp_data, OR_Rp_data, WA_Rp_data, CA_Rp_data, MT_Rp_data,
NJ_Rp_data, NM_Rp_data, SD_Rp_data, CA_Dp_data, MT_Dp_data, NJ_Dp_data, NM_Dp_data, ND_Dp_data, SD_Dp_data, DC_Dp_data]



#data name list of 538 results
dataNameList538 = ['AL_D', 'AL_R', 'AR_D', 'AR_R', 'AZ_D', 'AZ_R', 'CA_D', 'CA_R', 'CT_D', 'CT_R',
'FL_D', 'FL_R', 'GA_D', 'GA_R', 'IA_D', 'IA_R', 'IL_D', 'IL_R', 'IN_D', 'IN_R', 'KS_R',
'LA_D', 'LA_R', 'MA_D', 'MA_R', 'MD_D', 'MD_R', 'MI_D', 'MI_R', 'MO_D', 'MO_R', 'MS_D',
'NC_D', 'NC_R', 'NH_D', 'NH_R', 'NJ_D', 'NJ_R', 'NV_D', 'NV_R', 'NY_D', 'NY_R', 'OH_D',
'OH_R', 'OK_D', 'OK_R', 'PA_D', 'PA_R', 'RI_D', 'RI_R', 'SC_D', 'SC_R', 'TN_D', 'TN_R',
'TX_D', 'TX_R', 'UT_D', 'UT_R', 'VA_D', 'VA_R', 'VT_D', 'WI_D', 'WI_R', 'WV_D', 'WV_R']

#data list of PW results
dataNameListPW = ['IA_R', 'NH_R', 'SC_R', 'NV_R', 'AL_R', 'AK_R', 'AR_R', 'GA_R', 'MA_R',
'MN_R', 'OK_R', 'TN_R', 'TX_R', 'VA_R', 'KS_R', 'KY_R', 'LA_R', 'ME_R', 'PR_R',
'HI_R', 'ID_R', 'MI_R', 'MS_R', 'DC_R', 'FL_R', 'IL_R', 'MO_R', 'NC_R', 'OH_R',
'AZ_R', 'UT_R', 'IA_D', 'NH_D', 'NV_D', 'SC_D', 'AL_D', 'AR_D', 'CO_D', 'GA_D',
'MA_D', 'MN_D', 'OK_D', 'TN_D', 'TX_D', 'VT_D', 'VA_D', 'KS_D', 'LA_D', 'NE_D',
'ME_D', 'MI_D', 'MS_D', 'FL_D', 'IL_D', 'MO_D', 'NC_D', 'OH_D', 'AZ_D', 'UT_D',
'ID_D', 'AK_D', 'HI_D', 'WA_D', 'WI_R', 'WI_D', 'WY_D', 'NY_R', 'NY_D', 'CT_R',
'DE_R', 'MD_R', 'PA_R', 'RI_R', 'CT_D', 'DE_D', 'MD_D', 'PA_D', 'RI_D', 'IN_R',
'NE_R', 'WV_R', 'IN_D', 'WV_D', 'KY_D', 'OR_D', 'OR_R', 'WA_R', 'CA_R', 'MT_R',
'NJ_R', 'NM_R', 'SD_R', 'CA_D', 'MT_D', 'NJ_D', 'NM_D', 'ND_D', 'SD_D', 'DC_D']






#list of PW winners and stateIDs
#create a dictionary of stateID to state

StateID= {}

StateID['1533']='Iowa'
StateID['1534']='New Hampshire'
StateID['1553']='South Carolina'
StateID['1554']='Nevada'
StateID['1571']='Alabama'
StateID['1572']='Alaska'
StateID['1573']='Arkansas'
StateID['1575']='Georgia'
StateID['1576']='Massachusetts'
StateID['1577']='Minnesota'
StateID['1578']='Oklahoma'
StateID['1579']='Tennessee'
StateID['1580']='Texas'
StateID['1582']='Virginia'
StateID['1642']='Kansas'
StateID['1638']='Kentucky'
StateID['1639']='Louisiana'
StateID['1640']='Maine'
StateID['1641']='Puerto Rico'
StateID['1650']='Hawaii'
StateID['1651']='Idaho'
StateID['1652']='Michigan'
StateID['1653']='Mississippi'
StateID['1670']='District of Columbia'
StateID['1661']='Florida'
StateID['1660']='Illinois'
StateID['1662']='Missouri'
StateID['1663']='North Carolina'
StateID['1659']='Ohio'
StateID['1672']='Arizona'
StateID['1673']='Utah'


StateID['1541']='Iowa'
StateID['1540']='New Hampshire'
StateID['1606']='Nevada'
StateID['1607']='South Carolina'
StateID['1614']='Alabama'
StateID['1615']='Arkansas'
StateID['1616']='Colorado'
StateID['1617']='Georgia'
StateID['1618']='Massachusetts'
StateID['1619']='Minnesota'
StateID['1620']='Oklahoma'
StateID['1621']='Tennessee'
StateID['1622']='Texas'
StateID['1623']='Vermont'
StateID['1624']='Virginia'
StateID['1643']='Kansas'
StateID['1644']='Louisiana'
StateID['1645']='Nebraska'
StateID['1646']='Maine'
StateID['1649']='Michigan'
StateID['1648']='Mississippi'
StateID['1654']='Florida'
StateID['1655']='Illinois'
StateID['1656']='Missouri'
StateID['1657']='North Carolina'
StateID['1658']='Ohio'
StateID['1679']='Arizona'
StateID['1678']='Utah'
StateID['1681']='Idaho'
StateID['1686']='Alaska'
StateID['1687']='Hawaii'
StateID['1688']='Washington'
StateID['1703']='Wisconsin'
StateID['1695']='Wisconsin'
StateID['1696']='Wyoming'
StateID['1697']='New York'
StateID['1704']='New York'


StateID['1705']='Connecticut'
StateID['1706']='Delaware'
StateID['1707']='Maryland'
StateID['1708']='Pennsylvania'
StateID['1709']='Rhode Island'
StateID['1698']='Connecticut'
StateID['1699']='Delaware'
StateID['1700']='Maryland'
StateID['1701']='Pennsylvania'
StateID['1702']='Rhode Island'
StateID['1721']='Indiana'
StateID['1722']='Nebraska'
StateID['1723']='West Virginia'
StateID['1726']='Indiana'
StateID['1727']='West Virginia'
StateID['1728']='Kentucky'
StateID['1729']='Oregon'
StateID['1724']='Oregon'
StateID['1725']='Washington'
StateID['1741']='California'
StateID['1742']='Montana'
StateID['1743']='New Jersey'
StateID['1744']='New Mexico'
StateID['1745']='South Dakota'
StateID['1746']='California'
StateID['1751']='Montana'
StateID['1749']='New Jersey'
StateID['1752']='New Mexico'
StateID['1750']='North Dakota'
StateID['1748']='South Dakota'
StateID['1753']='District of Columbia'




Winners = {}
Winners['Alabama']=('Clinton','Trump')
Winners['Alaska']=('Sanders','Cruz')
Winners['Arkansas']=('Clinton','Trump')
Winners['Arizona']=('Clinton','Trump')
Winners['California']=('Clinton','Trump')
Winners['Colorado']=('Sanders','NA')
Winners['Connecticut']=('Clinton','Trump')
Winners['Delaware']=('Clinton','Trump')
Winners['Florida']=('Clinton','Trump')
Winners['Georgia']=('Clinton','Trump')
Winners['Hawaii']=('Sanders','Trump')
Winners['Idaho']=('Sanders','Cruz')
Winners['Iowa']=('Clinton','Cruz')
Winners['Illinois']=('Clinton','Trump')
Winners['Indiana']=('Sanders','Trump')
Winners['Kansas']=('Sanders','Cruz')
Winners['Kentucky']=('Clinton','Trump')
Winners['Louisiana']=('Clinton','Trump')
Winners['Massachusetts']=('Clinton','Trump')
Winners['Maine']=('Sanders','Cruz')
Winners['Maryland']=('Clinton','Trump')
Winners['Michigan']=('Sanders','Trump')
Winners['Minnesota']=('Sanders','Rubio')
Winners['Missouri']=('Clinton',' Trump')
Winners['Mississippi']=('Clinton','Trump')
Winners['Montana']=('Sanders','Trump')
Winners['Nebraska']=('Sanders','Trump')
Winners['North Carolina']=('Clinton','Trump')
Winners['North Dakota']=('Sanders','NA')
Winners['New Hampshire']=('Sanders',' Trump')
Winners['New Jersey']=('Clinton','Trump')
Winners['New Mexico']=('Clinton',' Trump')
Winners['Nevada']=('Clinton','Trump')
Winners['New York']=('Clinton','Trump')
Winners['Ohio']=('Clinton','Kasich')
Winners['Oklahoma']=('Sanders','Cruz')
Winners['Oregon']=('Sanders','Trump')
Winners['Pennsylvania']=('Clinton','Trump')
Winners['Rhode Island']=('Sanders','Trump')
Winners['South Carolina']=('Clinton','Trump')
Winners['South Dakota']=('Clinton','Trump')
Winners['Tennessee']=('Clinton','Trump')
Winners['Texas']=('Clinton','Cruz')
Winners['Utah']=('Sanders','Cruz')
Winners['Virginia']=('Clinton','Trump')
Winners['Vermont']=('Sanders','Trump')
Winners['Washington']=('Sanders','Trump')
Winners['Wisconsin']=('Sanders','Cruz')
Winners['West Virginia']=('Sanders','Trump')
Winners['Wyoming']=('Sanders','Cruz')
Winners['District of Columbia']=('Clinton','Rubio')
Winners['Puerto Rico']=('Clinton','Rubio')


######################################################################
# White/Black refer to the white/black dots, poll/kitchen refer to poll only/poll plus


#add data for 538
def adddata(pollHistory, pollWhite, pollBlack, kitchenHistory, kitchenWhite, kitchenBlack, dataname):
    i=0
    totallen = len(dataname["model"])
    # only want the larger sets
    while (i < totallen and (len(dataname["model"][i])>4)):
        i += 1
    if i==0:
        curWeight = 0
    else:
        #curWeight = float(1)/i  #can be changed for other metric
        curWeight = math.log(i)/i  #can be changed for other metric
    #print math.log(i+0.01) #checks the total weight of each state's result
    #print dataname["model"][0]["state"]
    #print i
    i=0
    #then go through the main code
    curpollHistory = [[]] #only contains 538 poll-only history, will be added to a huge list called pollHistory
    curkitchenHistory = [[]]
    while (i < totallen and (len(dataname["model"][i])>4)):
        curCandidate = dataname["model"][i]["candidate_name"]
        curState = dataname["model"][i]["state"]
        curPoll = dataname["model"][i]["pollonly_winprob"]
        curKitchen = dataname["model"][i]["kitchen_winprob"]
        # +43200 to add half a day for 538 so that predictions occur mid-day, to be fair
        curTime = mktime(datetime.strptime(dataname["model"][i]["forecastdate"],'%Y-%m-%d').timetuple())+43200
        
        #adding data to white and black lists
        if (Winners[curState][0]==curCandidate) or (Winners[curState][1]==curCandidate):
            pollWhite.append((curPoll,curWeight))
            kitchenWhite.append((curKitchen,curWeight))
        else:
            pollBlack.append((curPoll,curWeight))
            kitchenBlack.append((curKitchen,curWeight))


        #adding data to chart: curpollHistory
        #it has the structure [[name1, name2, name3],[(t,v)..],[...],[...]]
        if not curCandidate in curpollHistory[0]:
            curpollHistory[0].append(curCandidate)
            curkitchenHistory[0].append(curCandidate)
            curpollHistory.append([[curTime,curPoll]])
            curkitchenHistory.append([[curTime,curKitchen]])
        else:
            j = curpollHistory[0].index(curCandidate)
            curpollHistory[j+1].append([curTime,curPoll])
            curkitchenHistory[j+1].append([curTime,curKitchen])
   
        i += 1
    pollHistory.append(curpollHistory)
    kitchenHistory.append(curkitchenHistory)

#add data for PW
def adddataPW(PWHistory, pwWhite, pwBlack, dataname):
    curStateID = dataname["id"]
    #print curStateID
    curState = StateID[curStateID]
    #print curState
    #print Winners[curState][0]
    totallen=0
    for timeStamp in dataname["history"]:
        for candidateEntry in timeStamp["table"]:
            totallen += 1
    #print math.log(totallen)
    numCandidate = len(dataname["history"][0]["table"])
    effectiveLength = totallen/numCandidate
    #curWeight = math.log(effectiveLength)/effectiveLength*(numCandidate-1)
    curWeight = math.log(totallen)/totallen

    curPWHistory = [[]] #to be added to the longer list: PWHistory

    for timeStamp in dataname["history"]:
        curTime = mktime(datetime.strptime(timeStamp["timestamp"],'%m-%d-%Y %I:%M%p').timetuple())
        for candidateEntry in timeStamp["table"]:
            curCandidate = candidateEntry[0].split()[1]
            #print curCandidate
            curPW = int(candidateEntry[1][:-2])
            #print curPW
            if (Winners[curState][0]==curCandidate) or (Winners[curState][1]==curCandidate):
                #print curPW
                pwWhite.append((curPW,curWeight))
            else:
                pwBlack.append((curPW,curWeight))

            if not curCandidate in curPWHistory[0]:
                curPWHistory[0].append(curCandidate)
                curPWHistory.append([[curTime,curPW]])
            else:
                j = curPWHistory[0].index(curCandidate)
                curPWHistory[j+1].append([curTime,curPW])

    PWHistory.append(curPWHistory)



def windowAverage(numPoints, windowSize, lstWhite, lstBlack):
    returnlst = []
    for i in range(numPoints):
        midpoint = 100*(float(i)+0.5)/numPoints
        lower = midpoint - windowSize*0.5
        upper = midpoint + windowSize*0.5
        whiteCount = len([x[0] for x in lstWhite if (x[0]> lower and x[0] < upper)])
        blackCount = len([x[0] for x in lstBlack if (x[0]> lower and x[0] < upper)])
        whiteInWindow = [x for x in lstWhite if (x[0]> lower and x[0] < upper)]
        blackInWindow = [x for x in lstBlack if (x[0]> lower and x[0] < upper)]
        std = binomialStd(float(midpoint)/100, whiteCount+blackCount)
        avg = weightedAvg(whiteInWindow,blackInWindow)
        returnlst.append((midpoint,avg,std, whiteCount,blackCount))
    return returnlst


def tupleIntoLst2(listoftuples):
    xlst = []
    ylst = []
    for x in listoftuples:
        xlst.append(x[0])
        ylst.append(x[1])
    return (xlst,ylst)


def tupleIntoLst(listoftuples):
    xlst = []
    ylst = []
    zlst = []
    for x in listoftuples:
        xlst.append(x[0])
        ylst.append(x[1])
        zlst.append(x[2])
    return (xlst,ylst,zlst)

def weightedAvg(whiteInWindow, blackInWindow):
    if len(whiteInWindow)==0 and len(blackInWindow)==0:
        return float("inf")
    numerator = 0
    denominator = 0
    for x in whiteInWindow:
        numerator += x[1]
        denominator += x[1]
    for x in blackInWindow:
        denominator += x[1]
    return float(numerator)/denominator*100


def ratioWhite(numW, numB):
    if numW==0 and numB==0:
        return float("inf")
    else:
        return float(numW)/float(numW+numB)*100
        
def binomialStd(p, N):
    if p==0 or N==0:
        return 0
    else:
        return 100*(math.sqrt(N*p*(1-p)))/N


def logchoose(n, r):
    return math.log(math.factorial(n))-math.log(math.factorial(r))-math.log(math.factorial(n-r))

#pairwise subtract
def listSubtract (listA, listB):
    listC = []
    for i in range(len(listA)):
        listC.append(listA[i]-listB[i])
    return listC

#pairwise add
def listAdd (listA, listB):
    listC = []
    for i in range(len(listA)):
        listC.append(listA[i]+listB[i])
    return listC






def findNeighbors(value, arr):
    #must make sure value is within the range of arr
    rightNeighbor = min(x for x in arr if x > value)
    leftNeighbor = max(x for x in arr if x <= value)
    rightNeighborIndex = arr.index(rightNeighbor)
    leftNeighborIndex = arr.index(leftNeighbor)
    return (leftNeighborIndex, rightNeighborIndex)



# - returns floats: totalSpent, totalReturn, totalRisk, totalTrades 
# 
def calculateGains(stateAndParty, candidate, seriesA, seriesB):
    #buying or selling at market price B (PW), using price A(538) as reference

    In538 = stateAndParty in dataNameList538
    InPW = stateAndParty in dataNameListPW

    if In538:
        i = dataNameList538.index(stateAndParty)
        if candidate not in seriesA[i][0]:
            return ((float(0),float(0),float(0),0))
        j = seriesA[i][0].index(candidate)
        (tA,vA) =  tupleIntoLst2(seriesA[i][j+1])

    if InPW:
        i = dataNameListPW.index(stateAndParty)
        if candidate not in seriesB[i][0]:
            return ((float(0),float(0),float(0),0))
        j = seriesB[i][0].index(candidate)
        (tB, vB) = tupleIntoLst2(seriesB[i][j+1])

    if not (In538 and InPW):
        return [0,0,0,0]
        
    dataname = dataList[dataNameList538.index(stateAndParty)]
    curstate = dataname["model"][0]["state"]
    totalSpent = float(0)
    totalReturn = float(0)
    totalRisk = float(0)  #maximum possible money you can lose
    totalTrades = 0 #total number of trades
    if candidate in Winners[curstate]:
        finalPrice = float(100)
    else:
        finalPrice = float(0)

    minMargin = 0 #minimum margin before buying and selling
    
    for time in tB:
        if time > min(tA) and time < max(tA):
            (curLeftIndex, curRightIndex) = findNeighbors(time, tA)
            curPrice538 = vA[curLeftIndex]
            curPricePW = vB[tB.index(time)]
            if curPricePW <= curPrice538-minMargin: #buy at PW
                totalSpent += curPricePW
                totalReturn += finalPrice
                totalRisk += float(100)
                totalTrades += 1
            if curPricePW >= curPrice538+minMargin:  #sell at PW
                totalSpent += float(100)-curPricePW
                totalReturn += float(100)-finalPrice
                totalRisk += float(100)
                totalTrades += 1
            
    return [totalSpent, totalReturn, totalRisk, totalTrades]
    

def AllStateGain(pollHistory, kitchenHistory, PWHistory):
    totalPollSpent = float(0)
    totalPollReturn = float(0)
    totalPollRisk = float(0)
    totalPollTrades = 0
    totalKitchenSpent = float(0)
    totalKitchenReturn = float(0)
    totalKitchenRisk = float(0)
    totalKitchenTrades = 0
    for i in range(len(dataNameList538)):
        stateAndParty = dataNameList538[i]
        print stateAndParty
        for candidate in pollHistory[i][0]:
            print candidate
            (curPollSpent, curPollReturn, curPollRisk, curPollTrades) = calculateGains(stateAndParty, candidate, pollHistory, PWHistory)
            if curPollTrades == 0:
                curPollWeight = 0
            else:
                curPollWeight = math.log(curPollTrades)
            normPoll = curPollRisk+0.00001 #normalization constant for each (stateAndParty,candidate) pair, add .01 to avoid division by 0normalization
            totalPollSpent += curPollSpent/normPoll*curPollWeight
            totalPollReturn += curPollReturn/normPoll*curPollWeight
            totalPollRisk += curPollRisk/normPoll*curPollWeight
            totalPollTrades += curPollTrades
            (curKitchenSpent, curKitchenReturn, curKitchenRisk, curKitchenTrades) = calculateGains(stateAndParty, candidate, kitchenHistory, PWHistory)
            if curKitchenTrades == 0:
                curKitchenWeight = 0
            else:
                curKitchenWeight = math.log(curKitchenTrades)
            normKitchen = curKitchenRisk+0.00001 #normalization constant for each (stateAndParty,candidate) pair, add .01 to avoid division by 0normalization
            totalKitchenSpent += curKitchenSpent/normKitchen*curKitchenWeight
            totalKitchenReturn += curKitchenReturn/normKitchen*curKitchenWeight
            totalKitchenRisk += curKitchenRisk/normKitchen*curKitchenWeight
            totalKitchenTrades += curKitchenTrades
            print "------------"
            print str(stateAndParty)+" "+str(candidate)+" Poll investment: " + str((curPollSpent, curPollReturn, curPollRisk, curPollTrades))
            print str(stateAndParty)+" "+str(candidate)+" Kitchen investment: " + str((curKitchenSpent, curKitchenReturn, curKitchenRisk, curKitchenTrades))
    print "$$$$$$$$$$$$$$$$$$$"
    print "All states poll investment: "+ str((totalPollSpent,totalPollReturn,totalPollRisk,totalPollTrades))
    print "All states kitchen investment: "+ str((totalKitchenSpent,totalKitchenReturn,totalKitchenRisk,totalKitchenTrades))

def populateHistories():
    pollWhite = []
    pollBlack = []
    kitchenWhite = []
    kitchenBlack = []
    
    #declare global when modifying
    global pollHistory
    global kitchenHistory
    for x in dataList:
        adddata(pollHistory, pollWhite, pollBlack, kitchenHistory, kitchenWhite, kitchenBlack, x)
    ##########
    pwWhite = []
    pwBlack = []
    global PWHistory
    for x in dataListp:
        adddataPW(PWHistory, pwWhite, pwBlack, x)
    ########

def getStatePartyCandidates(stateChosen, partyChosen):
    candidateList = []
    stateAndParty = stateChosen+'_'+partyChosen
    if stateAndParty in dataNameList538:
        i = dataNameList538.index(stateAndParty)
        for candidate in pollHistory[i][0]:
            if candidate not in candidateList:
                candidateList.append(candidate)
    if stateAndParty in dataNameListPW:
        i = dataNameListPW.index(stateAndParty)
        for candidate in PWHistory[i][0]:
            if candidate not in candidateList:
                candidateList.append(candidate)
    return candidateList

# Flot time must be in epoch time, but in milliseconds
# Use this to convert epoch time from secs to milliseconds
# pointsArray is in structure of [[t0,y0],[t1,y1],[t2,y2]]
def toMillisecs(pointsArray):
    return [[p[0]*1000, p[1]] for p in pointsArray]
    
# saves the graphs of each candidate through time for every state
# saves investment gains for each candidate
def GetDataForCandidate(stateChosen, partyChosen, candidate):
    stateAndParty = stateChosen + '_' + partyChosen

    In538 = stateAndParty in dataNameList538
    InPW = stateAndParty in dataNameListPW

    threeGraphs = {'candidate':candidate, 'graphs':[], 'investmentDataPoll':[], 'investmentDataPlus':[]}
    
    if InPW:
        i = dataNameListPW.index(stateAndParty)
        if candidate in PWHistory[i][0]:
            j = PWHistory[i][0].index(candidate)
            threeGraphs['graphs'].append({'data': toMillisecs(PWHistory[i][j+1]), 'label':'PredictWise', 'color':'red'})
    
    if In538:
        i = dataNameList538.index(stateAndParty)
        if candidate in pollHistory[i][0]:
            j = pollHistory[i][0].index(candidate)
            threeGraphs['graphs'].append({'data': toMillisecs(pollHistory[i][j+1]), 'label':'538 Poll Only', 'color':'blue'})
            threeGraphs['graphs'].append({'data': toMillisecs(kitchenHistory[i][j+1]), 'label':'538 Poll Plus', 'color':'green'})

    threeGraphs['investmentDataPoll'].append(calculateGains(stateAndParty, candidate, pollHistory, PWHistory))
    threeGraphs['investmentDataPlus'].append(calculateGains(stateAndParty, candidate, kitchenHistory, PWHistory))
            
    return threeGraphs


# DJANGO VIEWS
# Create your views here.
def index(request):

    if request.method == 'POST':
        stateChosen = request.POST['stateChosen'].upper()
        partyChosen = request.POST['partyChosen']
        
        # populate histories if histories are empty
        if not pollHistory:
            populateHistories()
                
        response_data = {}
        response_data['stateLongName'] = request.POST['stateLongName']
        response_data['allCandidatesData'] = []
        
        # get all candidates for the state and party chosen
        targetCandidates = getStatePartyCandidates(stateChosen, partyChosen)
        #targetCandidates = ['Clinton']
        
        # get data for each candidate
        for candidate in targetCandidates:
            response_data['allCandidatesData'].append(GetDataForCandidate(stateChosen, partyChosen, candidate))
        
        #print "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
        #print response_data
        #print "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
        
        return HttpResponse(json.dumps(response_data), content_type="application/json")
        
    else:
        return render(request, 'index.html')

def info(request):

    pollData = [[1.0, 0.8561110992476114], [3.0, 5.547269491844374], [5.0, 5.068802720115255], [7.0, 0.0], [9.0, 1.741907844228439], [11.0, 5.2639143205759495], [13.0, 9.176179397495094], [15.0, 8.696982016360936], [17.0, 28.855884512585323], [19.0, 11.761620652011938], [21.0, 4.356431075560225], [23.0, 1.7740308047892137], [25.0, 12.587818168663079], [27.0, 0.0], [29.0, 25.617082193388658], [31.0, 51.06754458109677], [33.0, 62.832949528279535], [35.0, 30.651997052552748], [37.0, 37.246995672067285], [39.0, 83.01217179315957], [41.0, 55.72445551338055], [43.0, 20.064586327378024], [45.0, 16.18670204415046], [47.0, 43.76467307256889], [49.0, 48.42709999313669], [51.0, 60.46328792025949], [53.0, 77.89327292654428], [55.0, 85.48180707476108], [57.0, 91.48737978533022], [59.0, 31.406151588936225], [61.0, 43.118452024931095], [63.0, 90.04178637537933], [65.0, 80.84165045480167], [67.0, 57.66438595074829], [69.0, 49.838611410673174], [71.0, 75.56647328867828], [73.0, 97.59165628820085], [75.0, 87.5040331501415], [77.0, 92.49645819390814], [79.0, 89.39652502354726], [81.0, 86.45208390748839], [83.0, 80.24187767750904], [85.0, 92.01585592925375], [87.0, 83.69212385531142], [89.0, 93.1193037636533], [91.0, 100.0], [93.0, 100.0], [95.0, 92.67791787971069], [97.0, 87.86141888707967], [99.0, 95.8479741255268]]
    
    pollDiffData = [[1.0, -0.14388890075238858], [3.0, 2.547269491844374], [5.0, 0.06880272011525523], [7.0, -7.0], [9.0, -7.2580921557715605], [11.0, -5.7360856794240505], [13.0, -3.823820602504906], [15.0, -6.303017983639064], [17.0, 11.855884512585323], [19.0, -7.238379347988062], [21.0, -16.643568924439776], [23.0, -21.225969195210787], [25.0, -12.412181831336921], [27.0, -27.0], [29.0, -3.382917806611342], [31.0, 20.06754458109677], [33.0, 29.832949528279535], [35.0, -4.348002947447252], [37.0, 0.24699567206728545], [39.0, 44.01217179315957], [41.0, 14.724455513380548], [43.0, -22.935413672621976], [45.0, -28.81329795584954], [47.0, -3.2353269274311103], [49.0, -0.572900006863307], [51.0, 9.46328792025949], [53.0, 24.893272926544284], [55.0, 30.48180707476108], [57.0, 34.48737978533022], [59.0, -27.593848411063775], [61.0, -17.881547975068905], [63.0, 27.04178637537933], [65.0, 15.841650454801666], [67.0, -9.33561404925171], [69.0, -19.161388589326826], [71.0, 4.5664732886782815], [73.0, 24.591656288200852], [75.0, 12.504033150141495], [77.0, 15.49645819390814], [79.0, 10.396525023547255], [81.0, 5.452083907488387], [83.0, -2.758122322490962], [85.0, 7.015855929253746], [87.0, -3.307876144688578], [89.0, 4.119303763653306], [91.0, 9.0], [93.0, 7.0], [95.0, -2.322082120289309], [97.0, -9.138581112920335], [99.0, -3.152025874473196]]

    kitchenData = [[1.0, 1.4377316888604725], [3.0, 7.048643160834565], [5.0, 1.3009124720372327], [7.0, 2.3618472922138047], [9.0, 7.350289813585642], [11.0, 10.818230740707726], [13.0, 13.499232327839714], [15.0, 26.912317374557887], [17.0, 18.89888325909556], [19.0, 8.884182438018206], [21.0, 28.29894402803529], [23.0, 23.207544952454676], [25.0, 9.65817033105649], [27.0, 5.398018747122081], [29.0, 23.454942792607277], [31.0, 1.8835193578358647], [33.0, 44.472154788758246], [35.0, 35.9347828317096], [37.0, 35.06339673491151], [39.0, 34.741346848323765], [41.0, 41.46295298407332], [43.0, 61.04425658168891], [45.0, 44.344573188006876], [47.0, 68.58180341080431], [49.0, 49.27700784000476], [51.0, 50.92666372789011], [53.0, 60.300837529379336], [55.0, 58.478983395571774], [57.0, 82.72755604278905], [59.0, 90.67581359788409], [61.0, 56.24982130255478], [63.0, 97.11396287962218], [65.0, 79.43851116483664], [67.0, 75.03760987299368], [69.0, 79.17235549174353], [71.0, 49.92461070251612], [73.0, 93.1581102483223], [75.0, 77.51676447985575], [77.0, 57.54419458631014], [79.0, 64.40983073411151], [81.0, 88.35253554744203], [83.0, 75.06523301683686], [85.0, 63.33281458910458], [87.0, 73.5283144188061], [89.0, 86.53386560260775], [91.0, 86.6157415957359], [93.0, 95.65919043966242], [95.0, 97.80948786136808], [97.0, 87.34331673566695], [99.0, 95.60731626579167]]

    kitchenDiffData = [[1.0, 0.43773168886047253], [3.0, 4.048643160834565], [5.0, -3.6990875279627673], [7.0, -4.638152707786196], [9.0, -1.6497101864143584], [11.0, -0.18176925929227394], [13.0, 0.4992323278397137], [15.0, 11.912317374557887], [17.0, 1.8988832590955589], [19.0, -10.115817561981794], [21.0, 7.29894402803529], [23.0, 0.20754495245467552], [25.0, -15.34182966894351], [27.0, -21.60198125287792], [29.0, -5.545057207392723], [31.0, -29.116480642164134], [33.0, 11.472154788758246], [35.0, 0.9347828317095974], [37.0, -1.9366032650884932], [39.0, -4.258653151676235], [41.0, 0.4629529840733184], [43.0, 18.044256581688913], [45.0, -0.6554268119931237], [47.0, 21.581803410804312], [49.0, 0.27700784000475664], [51.0, -0.07333627210989135], [53.0, 7.300837529379336], [55.0, 3.478983395571774], [57.0, 25.727556042789047], [59.0, 31.675813597884087], [61.0, -4.750178697445222], [63.0, 34.11396287962218], [65.0, 14.43851116483664], [67.0, 8.037609872993684], [69.0, 10.17235549174353], [71.0, -21.07538929748388], [73.0, 20.158110248322302], [75.0, 2.516764479855752], [77.0, -19.45580541368986], [79.0, -14.590169265888491], [81.0, 7.352535547442031], [83.0, -7.9347669831631435], [85.0, -21.66718541089542], [87.0, -13.471685581193896], [89.0, -2.4661343973922527], [91.0, -4.384258404264102], [93.0, 2.6591904396624244], [95.0, 2.8094878613680834], [97.0, -9.656683264333054], [99.0, -3.392683734208333]]
    
    pwData = [[1.0, 0.06252612102567032], [3.0, 1.8776825544611797], [5.0, 1.6631717292443904], [7.0, 6.492804158857954], [9.0, 9.23284020033909], [11.0, 6.8816886008407625], [13.0, 0.6610375773276871], [15.0, 4.124333186525744], [17.0, 13.700562800252133], [19.0, 13.029021982939348], [21.0, 22.297909795273984], [23.0, 27.791190936932704], [25.0, 18.38447124967611], [27.0, 21.202484543633776], [29.0, 27.235912597364887], [31.0, 19.364744392381244], [33.0, 23.92488461163203], [35.0, 18.47707846516182], [37.0, 44.21315668802338], [39.0, 25.774099725719513], [41.0, 34.71917890444274], [43.0, 31.657549741402356], [45.0, 34.43077859076431], [47.0, 43.963388170320044], [49.0, 26.707518068673753], [51.0, 68.80511150949614], [53.0, 37.354810747272474], [55.0, 63.964290324631875], [57.0, 57.23685917448243], [59.0, 74.79151106740287], [61.0, 71.74303062775678], [63.0, 77.13740057953993], [65.0, 86.06250133306986], [67.0, 72.1983726126027], [69.0, 84.49269633354648], [71.0, 83.31576486379724], [73.0, 81.965424941056], [75.0, 88.93584919979168], [77.0, 79.23972057963732], [79.0, 79.2617811239536], [81.0, 82.73661607957014], [83.0, 84.33765174695137], [85.0, 92.64874872509759], [87.0, 98.39517454232522], [89.0, 96.01211779395491], [91.0, 81.00125321516832], [93.0, 86.02388644360214], [95.0, 94.87993839845129], [97.0, 94.26196602027136], [99.0, 97.68345367757696]]
    
    pwDiffData = [[1.0, -0.9374738789743297], [3.0, -1.1223174455388203], [5.0, -3.3368282707556096], [7.0, -0.5071958411420461], [9.0, 0.23284020033909059], [11.0, -4.1183113991592375], [13.0, -12.338962422672314], [15.0, -10.875666813474256], [17.0, -3.2994371997478673], [19.0, -5.970978017060652], [21.0, 1.2979097952739842], [23.0, 4.791190936932704], [25.0, -6.6155287503238895], [27.0, -5.797515456366224], [29.0, -1.7640874026351128], [31.0, -11.635255607618756], [33.0, -9.07511538836797], [35.0, -16.52292153483818], [37.0, 7.213156688023382], [39.0, -13.225900274280487], [41.0, -6.280821095557258], [43.0, -11.342450258597644], [45.0, -10.569221409235688], [47.0, -3.0366118296799556], [49.0, -22.292481931326247], [51.0, 17.805111509496143], [53.0, -15.645189252727526], [55.0, 8.964290324631875], [57.0, 0.23685917448243288], [59.0, 15.791511067402865], [61.0, 10.74303062775678], [63.0, 14.137400579539928], [65.0, 21.06250133306986], [67.0, 5.198372612602697], [69.0, 15.492696333546476], [71.0, 12.315764863797241], [73.0, 8.965424941056], [75.0, 13.935849199791676], [77.0, 2.2397205796373214], [79.0, 0.26178112395359676], [81.0, 1.7366160795701404], [83.0, 1.3376517469513658], [85.0, 7.64874872509759], [87.0, 11.395174542325222], [89.0, 7.012117793954914], [91.0, -9.998746784831681], [93.0, -6.976113556397863], [95.0, -0.12006160154871282], [97.0, -2.738033979728641], [99.0, -1.3165463224230365]]
    
    chartsData = [pollData, pollDiffData, kitchenData, kitchenDiffData, pwData, pwDiffData]

    return render(request, 'info.html', {'chartsData': chartsData})
    
def sourcecode(request):
    return render(request, 'sourcecode.html')
    
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

