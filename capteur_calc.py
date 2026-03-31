
freq_hz_array = [1000000, 100000, 1000]

time_ms = 2
dist_cm = 8
dist_m = dist_cm / 100
time_s = time_ms / 1000

for freq_hz in freq_hz_array:

    print()
    print("--", freq_hz / 1000,"kHz --")

    shot_nb = freq_hz * time_s
    print("shot number :", shot_nb)

    dist_step = dist_m / shot_nb
    print("Step distance :", dist_step, "m")

    dist_step_um = dist_step * 1000
    print("setp distance", dist_step_um, "mm")

    print("-----")
    print()
