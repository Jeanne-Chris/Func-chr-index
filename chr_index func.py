# This is a function that divides and groups the alphabet capital letters according to a given input integer. 

all_chr = [chr(alphabet) for alphabet in range(0, 255)]
print()
print(all_chr)
print(f"chr(97) is the index of", chr(65))
print(f"chr(123) is the index of", chr(90))
print()


def grouped_alpha(num):
    alist = [chr(alphabet) for alphabet in range(65, 91)]
    cuts = int(26/num)
    if 26%num != 0:              # to print input int 3 and up
        cuts += 1
        for l in range(cuts):
            print(alist[:num])
            del alist[:num]
    else:
        for l in range(cuts):    # to print input int 1 and 2
            print(alist[:num])
            del alist[:num]


input_num = int(input("Enter a number between 1 and 26 here: "))


grouped_alpha(input_num)

