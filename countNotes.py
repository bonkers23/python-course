# M1L4 Activity 2
# Topic: Count the Notes
# This program counts the number of notes for a given amount

amount = 786

note_100 = amount // 100
remaining = amount % 100

note_50 = remaining // 50
remaining = remaining % 50

note_10 = remaining // 10

print("Total Amount:", amount)
print("100 rupee notes:", note_100)
print("50 rupee notes:", note_50)
print("10 rupee notes:", note_10)

# End of program
