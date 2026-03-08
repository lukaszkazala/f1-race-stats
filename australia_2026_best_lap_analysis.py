import os
import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt

fastf1.plotting.setup_mpl(mpl_timedelta_support=False, color_scheme="fastf1")

cache_path = "D:/Portfolio/f1-linkedin/cache"
os.makedirs(cache_path, exist_ok=True)
fastf1.Cache.enable_cache(cache_path)

session = fastf1.get_session(2026, "Australian Grand Prix", "R")
session.load(laps=True, telemetry=True, weather=False, messages=False)

russell_lap = session.laps.pick_drivers("RUS").pick_fastest()
antonelli_lap = session.laps.pick_drivers("ANT").pick_fastest()
leclerc_lap = session.laps.pick_drivers("LEC").pick_fastest()

rus_tel = russell_lap.get_car_data().add_distance()
ant_tel = antonelli_lap.get_car_data().add_distance()
lec_tel = leclerc_lap.get_car_data().add_distance()

# kolory ręczne
driver_colors = {
    "Russell": "darkblue",     
    "Antonelli": "lightblue",  
    "Leclerc": "red"   
}

plt.figure(figsize=(15, 8))

plt.plot(rus_tel["Distance"], rus_tel["Speed"], label="Russell", color=driver_colors["Russell"], linewidth=2.5)
plt.plot(ant_tel["Distance"], ant_tel["Speed"], label="Antonelli", color=driver_colors["Antonelli"], linewidth=2.5)
plt.plot(lec_tel["Distance"], lec_tel["Speed"], label="Leclerc", color=driver_colors["Leclerc"], linewidth=2.5)

plt.title("Australian GP 2026 - Best Lap Speed Comparison", fontsize=16, pad=15)
plt.xlabel("Distance [m]", fontsize=12)
plt.ylabel("Speed [km/h]", fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# zamiana czasu na czytelny format
rus_time = str(russell_lap["LapTime"])[10:-3]
ant_time = str(antonelli_lap["LapTime"])[10:-3]
lec_time = str(leclerc_lap["LapTime"])[10:-3]

info_text = (
    f"Best laps:\n"
    f"Russell   {rus_time}\n"
    f"Antonelli {ant_time}\n"
    f"Leclerc   {lec_time}"
)

plt.gca().text(
    1.02, 0.95, info_text,
    transform=plt.gca().transAxes,
    fontsize=11,
    verticalalignment="top",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#1e1e1e", alpha=0.85)
)

plt.savefig(r"D:\Portfolio\f1-linkedin\best_laps_Melbourne\images\best_lap_speed.png", dpi=300, bbox_inches="tight")
plt.tight_layout()
plt.show()