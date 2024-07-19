RBC_Count = float(input("enter rbc count"))
Haemoglobin = float(input("enter haemoglobin"))
Total_WBC_COUNT = float(input("enter wbc count"))
Platelets_Count = float(input("enter platelets count"))
PCV = float(input("enter pcv"))
Blood_Sugar = float(input("enter blood sugar"))
Blood_Urea = float(input("enter blood urea"))
S_Creatinine = float(input("enter s.creatinine"))
MCV = float(input("enter mcv"))
MCH = float(input("enter mch"))


if (RBC_Count>=4.5) and (RBC_Count<=5.5):
    print("the RBC count is Normal")
else:
    print("the Rbc count is abnormal")


if (Haemoglobin>=13) and (Haemoglobin<=17):
    print("the Haemoglobin level is normal")
else:
    print("the haemoglobin level is abnormal")


if (Total_WBC_COUNT>=4000) and (Total_WBC_COUNT<=11000):
    print("the WBC count is normal")
else:
    print("the WBC count is abnormal")


if (Platelets_Count>=1.5) and (Platelets_Count<=4.5):
    print("the platelets count is normal")
else:
    print("the platelets count is abnormal")


if (PCV>=40) and (PCV<=54):
    print("the pcv is normal")
else:
    print("the pcv is abnormal")


if (Blood_Sugar>=80) and (Blood_Sugar<=140):
    print("the blood sugar is normal")
else:
    print("the blood sugar is abnormal")


if (Blood_Urea>=15) and (Blood_Urea<=45):
    print("the blood urea is normal")
else:
    print("the blood urea is abnormal")


if (S_Creatinine>=0.6) and (S_Creatinine<=1.2):
    print("the s.creatinine is normal")
else:
    print("the s.creatinine is abnormal")


if (MCV>=80) and (MCV<=100):
    print("the mcv is normal")
else:
    print("the mcv is abnormal")


if (MCH>=27) and (MCH<=32):
    print("the mch is normal")
else:
    print("the mch is abnormal")