# input hours
front = ('Dare', 'Esther', 'Chioma', 'Bayo', 'Chinanza')
back = ['Alex', 'Richard', 'Timi', 'Feston', 'Justice', 'Samuel']
Others = ['Janiel', 'John']
f_hours = []
b_hours = []
Tip = []
FTTP = []
BTTP = []
print('Please enter hours for front workers')
for i in range(len(front)):
    while True:
        try:
            hrf = float(input('{}: '.format(front[i])))
            if hrf <= 0:
                raise ValueError('stop')
            break
        except ValueError:
            print('Hours cannot be less than 0')
    f_hours.append(hrf)
Front_total_hours = f_hours[0]+f_hours[1]+f_hours[2]+f_hours[3]+f_hours[4]
print('Front total hours =', f_hours[0]+f_hours[1]+f_hours[2]+f_hours[3]+f_hours[4])

print()
print('Please enter hours for back workers')
for i in range(len(back)):
    while True:
        try:
            hrb = float(input('{}: '.format(back[i])))
            if hrb <= 0:
                raise ValueError('stop')
            break
        except ValueError:
            print('Hours cannot be less than 0')
    b_hours.append(hrb)
Back_total_hours = b_hours[0]+b_hours[1]+b_hours[2]+b_hours[3]+b_hours[4]+b_hours[5]
print('Back total hours =', b_hours[0]+b_hours[1]+b_hours[2]+b_hours[3]+b_hours[4]+b_hours[5])

print()
print('Please enter Tip for front workers')
for i in range(len(front)):
    while True:
        try:
            tp = float(input('{}: '.format(front[i])))
            if tp <= 0:
                raise ValueError('stop')
            break
        except ValueError:
            print('Tip cannot be less than 0')
    Tip.append(tp)

Total_Tip = Tip[0]+Tip[1]+Tip[2]+Tip[3]+Tip[4]
Front_Tip = 0.7*Total_Tip
Front_per_hr = Front_Tip/Front_total_hours
Back_Tip = 0.3*Total_Tip
Back_per_hr = Back_Tip/Back_total_hours
print()
print('Total Tip =', Tip[0]+Tip[1]+Tip[2]+Tip[3]+Tip[4])
print('Front Tip =', 0.7*Total_Tip)
print('Front Tip Per Hr =', Front_per_hr)
print('Back Tip =', 0.3*Total_Tip)
print('Back Tip Per Hr =', Back_per_hr)
print()

print('Front Tip per Hr =', Front_per_hr)
print()
for i in range(len(front)):
    tpp = f_hours[i] * Front_per_hr
    FTTP.append(tpp)
for i in range(len(back)):
    bpp = b_hours[i] * Front_per_hr
    BTTP.append(bpp)

print('{:<20} {:>20} {:>20}'.format('Front Workers', 'hours', 'Tip'))
for i in range(len(front)):
    print('{:<20} {:>20.2f} {:>20.2f}'.format(front[i], f_hours[i], FTTP[i]))
print()
print('{:<20} {:>20} {:>20}'.format('Back Workers', 'hours', 'Tip'))
for i in range(len(front)):
    print('{:<20} {:>20.2f} {:>20.2f}'.format(back[i], b_hours[i], BTTP[i]))
