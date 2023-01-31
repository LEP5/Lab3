import random
import time

Activity1 = "סיור גדר"
Activity2 = "בדיקת מעברים + שערים"
Activity3 = "השלמת תצפית"
Activity4 = "תגבור ש.ג"
Activity5 = "מתקנים חיוניים"
Activity6 = "בדיקת שערים"
Activity7 = "בדיקת מעברי מים"
ActivityList = [Activity1, Activity2, Activity3, Activity4, Activity5, Activity6, Activity7]
Hours = ["05:45", "07:30", "09:15", '11:00', '13:20', '16:30', '18:30', '22:15', '01:00', '02:00', '05:10']
#ActivityNum = input('How many activities per day do you want to perform? ')
#for i in range(ActivityNum):
#    Hours.append(input('Insert hour ' + str(HoursCount)))
#    HourCount == int(HourCount)+1
ActivityNum = 10
HourCount = 0
Row = []
print('========================')
for i in range(0, 11):
    time.sleep(0.5)
    if HourCount == 0:
        print('|' + 'פתיחת ציר' + '|' + Hours[HourCount])
        HourCount += 1
        time.sleep(0.1)
    elif HourCount == 5:
        print('|' + 'סגירת ציר' + '|' + Hours[HourCount])
        HourCount += 1
    else:
        Row = ('|' + (ActivityList[random.randrange(0, 6)] + '|'))
        print (str(Row).replace(",", "")+Hours[HourCount])
        HourCount += 1

print('========================')

