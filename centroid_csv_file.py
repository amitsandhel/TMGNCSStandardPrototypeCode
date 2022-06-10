import csv
with open("zone_centriods_map.csv", mode = 'r') as station_centroid:
    with open("zone_centriods.csv", mode="r") as region_centroid:
        station_centroid_file = csv.reader(station_centroid)
        region_centroid_file = csv.reader(region_centroid)
        next(station_centroid_file)
        station_centroids_dict = {}
        old_zone_centroid_list = []
        new_zone_centroid_list = []
        full_centroids_dict = {}
        for centroids in station_centroid_file:
            old_ncs_station_centroid = int(centroids[2])
            new_ncs__station_centroid  = int(centroids[3])
            if int(old_ncs_station_centroid) != 0  and int(new_ncs__station_centroid) != 0:
                station_centroids_dict[old_ncs_station_centroid] = new_ncs__station_centroid
        next(region_centroid_file)
        for regions in region_centroid_file:
            old_ncs_region_centroid_range = range(int(regions[2]), int(regions[1])-1, -1)
            new_ncs__region_centroid_range  =  range(int(regions[4]), int(regions[3])-1, -1)
            old_zone_centroid_list.append([x for x in old_ncs_region_centroid_range])
            new_zone_centroid_list.append([x for x in new_ncs__region_centroid_range])
        for i in range(len(old_zone_centroid_list)):
            new_dict = {old_zone_centroid_list[i][j]: new_zone_centroid_list[i][j] for j in range(len(old_zone_centroid_list[i]))}
            full_centroids_dict = station_centroids_dict | new_dict
        print(full_centroids_dict)