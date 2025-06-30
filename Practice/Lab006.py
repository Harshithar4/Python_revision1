pali ="MaDam"
pali1=pali.lower()
print(pali1)
rev_pali = ""
for i in pali1:
    rev_pali = i + rev_pali
if rev_pali == pali1:
    print("It is Palindrome")
else:
    print("It is not a Palindrome")