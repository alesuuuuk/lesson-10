# # task 1
# def formattedText(author):
#     text = """\
# "Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself."
# {}"""
#     print(text.format(author))
#
# if __name__ == "__main__":
#     author_name = "Bill Gates"
#     formattedText(author_name)
#
#
# # task 2
#
# def evenOdd(begin, end):
#     even_numbers = []
#     odd_numbers = []
#     for i in range(begin, end+1):
#         if i%2 == 0:
#             even_numbers.append(i)
#         else:
#             odd_numbers.append(i)
#
#     print(f"{even_numbers}  - all even numbers in range from {begin} to {end}")
#     print(f"{odd_numbers}  - all odd numbers in range from {begin} to {end}")
#
#
# if __name__ == "__main__":
#     while True:
#         choice = input("continue(con) or exit(ex)")
#         if choice == "con":
#             begin_range = int(input("type begin of range"))
#             end_range = int(input("type end of range"))
#             evenOdd(begin_range, end_range)
#         elif choice == "ex":
#             break
#         else:
#             print("u're invalid or what? try again")
#
#
# # task 3
#
# def drawSquare(side_length, symbol, fill=True):
#     if fill:
#         for _ in range(side_length):
#             print(symbol * side_length)
#     else:
#         for i in range(side_length):
#             if i == 0 or i == side_length - 1:
#                 print(symbol * side_length)
#             else:
#                 print(symbol + ' ' * (side_length - 2) + symbol)
#
# if __name__ == "__main__":
#     while True:
#         choice = input("continue(con) or exit(ex)")
#         if choice == "con":
#             side_length = int(input("Enter the side length of the square: "))
#             symbol = input("Enter the symbol for the square: ")
#             is_filled = input("Enter 'True' for a filled square or 'False' for an empty square: ").lower()
#
#             if is_filled == 'true':
#                 drawSquare(side_length, symbol, fill=True)
#             elif is_filled == 'false':
#                 drawSquare(side_length, symbol, fill=False)
#             else:
#                 print("Invalid input. Please enter 'True' or 'False'.")
#
#         elif choice == "ex":
#             break
#         else:
#             print("invalid syntax try again")
#
#
# # task 4
#
# def findMin(*args):
#     min_num = args[0]
#     for num in args:
#         if num < min_num:
#             min_num = num
#     return min_num
#
# if __name__ == "__main__":
#     while True:
#         choice = input("continue(con) or exit(ex)")
#         if choice == "con":
#             num1 = int(input("Enter the first number: "))
#             num2 = int(input("Enter the second number: "))
#             num3 = int(input("Enter the third number: "))
#             num4 = int(input("Enter the fourth number: "))
#             num5 = int(input("Enter the fifth number: "))
#             result = findMin(num1, num2, num3, num4, num5)
#             print("The minimum number is:", result)
#         elif choice == "ex":
#             break
#         else:
#             print("invalid syntax try again")
#
#
#
#
#
#
#
#
# # task 5
#
#
# def dobutok(begin, end):
#     if begin > end:
#         true_begin = end
#         true_end = begin
#         begin = true_begin
#         end = true_end
#         for i in range(begin, end+1):
#             for j in range(begin, end+1):
#                 print(i*j)
#     elif begin < end:
#         for i in range(begin, end+1):
#             for j in range(begin, end+1):
#                 print(i*j)
#
#
#
# if __name__ == "__main__":
#     while True:
#         choice = input("continue(con) or exit(ex)")
#         if choice == "con":
#             begin_range = int(input("type begin of range"))
#             end_range = int(input("type end of range"))
#             dobutok(begin_range, end_range)
#         elif choice == "ex":
#             break
#         else:
#             print("invalid syntax try again")
#
#
# # task 6
#
#
# def lenNumbers(nums):
#     print(len(str(nums)))
#
# if __name__ == "__main__":
#     while True:
#         choice = input("continue(con) or exit(ex)")
#         if choice == "con":
#             number = int(input("type number"))
#             lenNumbers(number)
#         elif choice == "ex":
#             break
#         else:
#             print("invalid syntax try again")


# task 7


def palindromNumber(num):
    reverse_number = str(num)
    reverse_number = reverse_number[::-1]
    print(reverse_number)

if __name__ == '__main__':
    while True:
        choice = input("continue(con) or exit(ex)")
        if choice == "con":
            number = int(input("dsdadad"))
            palindromNumber(number)
        elif choice == "ex":
            break
        else:
            print("invalid syntax try again")