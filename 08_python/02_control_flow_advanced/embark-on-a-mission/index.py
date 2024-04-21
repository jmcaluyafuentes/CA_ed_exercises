# have_supplies : boolean
# distance_to_mission_site : integer
# fuel_in_vehicle : integer
def ready_to_embark_on_mission(have_supplies, distance_to_mission_site, fuel_in_vehicle):
    pass
    if have_supplies:
        if distance_to_mission_site <= 10 or fuel_in_vehicle >= distance_to_mission_site:
            return True
    else:
        return False
