"""matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
]
primary_sum=0
for i in range(len(matrix)):
    primary_sum+=matrix[i][i]
print("primary diagonal sum",primary_sum)""",

"""products=[{
"product_number":1,
"product_name":"mertin_AMK",
"product_seri_number":2185265756,
},
{
"product_number":1,
"product_name":"Mustafanınki_daha_büyük",
"product_seri_number":0,
},
{
"product_number":3,
"product_name":"caffee",
"product_seri_number":01,
}
]"""



product=[{
"product_id":3,
"product_name":"coffee",
"product_price":18000,
},
{
"product_id":2,
"product_name":"dehre",
"product_price":29000
},
]
matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15, 16]
]

n = len(matrix)
primary_sum = 0
secondary_sum = 0

for i in range(n):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][n - 1 - i]

total_diagonal_sum = primary_sum + secondary_sum

if n % 2 == 1:
    center = matrix[n // 2][n // 2]
    total_diagonal_sum -= center

print("Primary diagonal sum :", primary_sum)
print("Secondary diagonal sum:", secondary_sum)
print("Total (without double center):", total_diagonal_sum)
