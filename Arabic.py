import time
from plyer import notification

adhkar = [
    "سبحان الله",
    "الحمد لله",
    "الله أكبر",
    "لا إله إلا الله",
    "استغفر الله"
]

# عدد الدورات
num_cycles = 2

# دورة لعرض الأذكار
for _ in range(num_cycles):
    for dhikr in adhkar:
        notification.notify(
            title="ذكر الله",
            message=dhikr,
            timeout=10
        )
        time.sleep(5)
