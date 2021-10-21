import statistics
import pandas as pd
import csv
df=pd.read_csv("data.csv")

height_list=df["Height"].to_list()
weight_list=df["Weight"].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

print("mean,median and mode of height is {},{} and {}".format(height_mean,height_median,height_mode))

print("mean,median and mode for weight is {},{} and {}".format(height_mean,height_median,height_mode))

height_standardDivision=statistics.stdev(height_list)
weight_standardDivision=statistics.stdev(weight_list)

height_first_standard_division_start,height_first_standard_division_end=height_mean-height_standardDivision,height_mean+height_standardDivision 
height_second_standard_division_start,height_second_standard_division_end=height_mean-(2*height_standardDivision),height_mean+(2*height_standardDivision)
height_third_standard_division_start,height_third_standard_division_end=height_mean-(3*height_standardDivision),height_mean+(3*height_standardDivision)\

weight_first_standard_division_start,weight_first_standard_division_end=weight_mean-weight_standardDivision,weight_mean+weight_standardDivision 
weight_second_standard_division_start,weight_second_standard_division_end=weight_mean-(2*weight_standardDivision),weight_mean+(2*weight_standardDivision)
weight_third_standard_division_start,weight_third_standard_division_end=weight_mean-(3*weight_standardDivision),weight_mean+(3*weight_standardDivision)

height_list_within_1standardDivisision=[result for result in height_list if result>height_first_standard_division_start and result<height_first_standard_division_end]
height_list_within_2standardDivisision=[result for result in height_list if result>height_second_standard_division_start and result<height_second_standard_division_end]
height_list_within_3standardDivisision=[result for result in height_list if result>height_third_standard_division_start and result<height_third_standard_division_end]

weight_list_within_1standardDivisision=[result for result in weight_list if result>weight_first_standard_division_start and result<weight_first_standard_division_end]
weight_list_within_2standardDivisision=[result for result in weight_list if result>weight_second_standard_division_start and result<weight_second_standard_division_end]
weight_list_within_3standardDivisision=[result for result in weight_list if result>weight_third_standard_division_start and result<weight_third_standard_division_end]

print("{} % of data for height within 1 standard division".format(len(height_list_within_1standardDivisision)*100.0/len(height_list)))
print("{} % of data for height within 2 standard division".format(len(height_list_within_2standardDivisision)*100.0/len(height_list)))
print("{} % of data for height within 3 standard division".format(len(height_list_within_3standardDivisision)*100.0/len(height_list)))

print("{} % of data for weight within 1 standard division".format(len(weight_list_within_1standardDivisision)*100.0/len(weight_list)))
print("{} % of data for weight within 2 standard division".format(len(weight_list_within_2standardDivisision)*100.0/len(weight_list)))
print("{} % of data for weight within 3 standard division".format(len(weight_list_within_3standardDivisision)*100.0/len(weight_list)))
