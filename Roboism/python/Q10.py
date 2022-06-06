fst_numb = int(input("Enter some random number = "))

scnd_numb = int(input("Enter some random number = "))

fst_numb = fst_numb ^ scnd_numb

scnd_numb = fst_numb ^ scnd_numb

fst_numb = fst_numb ^ scnd_numb

print("The Result After Swapping  given two Numbers is:")
print("First Number = ", fst_numb)
print("Second Number = ", scnd_numb)