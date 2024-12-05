def get_sqr_val(x):
    return (x*x)
def get_sum_of_sqrs(list_x):
    sum=0
    for i in list_x:
        sum+=get_sqr_val(i)
    return sum
list_x=[1,2,3,4]
sum_of_sqrs=get_sum_of_sqrs(list_x)
print(sum_of_sqrs)
