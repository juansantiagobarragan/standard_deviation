import math 
a = [.22,-.41,-.16,.03,.23,.23,.28,-.06,-.2,.07,-1.2]
sdforeachlist = []
squaredsd = []
sumofall = 0
sdforeach = 0
sumofallsd = 0
variance = 0
roundedsdforeach = 0
for x in a:
    sumofall = sumofall + x
avg = sumofall/len(a)
roundavg = round(avg,1)
for x in a:
    sdforeach = x - roundavg
    roundedsdforeach=round(sdforeach,1)
    sdsquared = pow(roundedsdforeach,2)
    sdforeachlist.append(sdsquared)
for x in sdforeachlist:
    sumofallsd = sumofallsd + x
variance = sumofallsd / (len(a)-1)
print(round(math.sqrt(variance),2))