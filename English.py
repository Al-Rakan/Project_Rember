import time
from plyer import notification

adhkar = [
    "SubhanAllah",
    "Alhamdulillah",
    "Allahu Akbar",
    "La ilaha illallah",
    "Astaghfirullah"
]

# Number of cycles
num_cycles = 2

# Loop to display adhkar
for _ in range(num_cycles):
    for dhikr in adhkar:
        notification.notify(
            title="Dhikr Reminder",
            message=dhikr,
            timeout=10
        )
        time.sleep(5)
