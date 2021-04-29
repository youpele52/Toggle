-- ACCESS TO PUBLIC DATABASES


-- Question 1: Citibike Stations

--1A: what is the average station capacity?
--Answer : 31.53 bikes
-- Query 

  SELECT
    AVG(capacity) as Average_station_capacity
  FROM
    `bigquery-public-data.new_york_citibike.citibike_stations`


--1B: in the current data, what proportion of total bikes in the network are in use?
--Answer: 937 bikes
--Query 

  SELECT 
  COUNT(CASE when is_renting = True then 'in_use' end ) Total_bikes_in_use
    
  FROM
    `bigquery-public-data.new_york_citibike.citibike_stations`





-- Question 2: Citibike Trips

--2A: what is the average trip length over the last month?
--Answer : 1121.91 s
--Query 
SELECT
AVG(tripduration) Average_trip_duration
FROM `bigquery-public-data.new_york_citibike.citibike_trips` 
where  CAST(starttime as DATE) >= '2018-05-01'





--2B: of trips that originated or ended on Broadway, please provide a breakdown of ridership
    Usertype
    birth_year

--Answer: Query
SELECT
usertype, birth_year, start_station_name, end_station_name,  CAST(starttime as DATE) as start_date
FROM `bigquery-public-data.new_york_citibike.citibike_trips` 
where  CAST(starttime as DATE) >= '2018-05-01'
 and (start_station_name like '%Broadway%' or end_station_name like '%Broadway%')

# order by CAST(starttime as DATE) asc


--2C: For those same trips, what was the most common direction of travel. Please express your answer as one of four choices - NE, SE, NW, SW
-- Answer: NW, 179006 traveled in NW direction.
--Querry

SELECT 
count(CASE when end_station_latitude >=0 and  end_station_longitude >= 0 and end_station_name like '%Broadway%' then 'NE' END ) as NE_total_trips,
count(CASE when end_station_latitude >=0 and  end_station_longitude <= 0 and end_station_name like '%Broadway%' then 'NW' END ) as NW_total_trips,
count(CASE when end_station_latitude <=0 and  end_station_longitude >= 0 and end_station_name like '%Broadway%' then 'SE' END ) as SE_total_trips,
count(CASE when end_station_latitude <=0 and  end_station_longitude <= 0 and end_station_name like '%Broadway%' then 'SW' END ) as SW_total_trips

FROM `bigquery-public-data.new_york_citibike.citibike_trips` 
where  CAST(starttime as DATE) >= '2018-05-01'





