total_candy = bagA + bagB + bagC
print(f"Total candy collected: {total_candy}")


# Part 2: Fair sharing (include yourself)
people += 1
share = total_candy//people
leftover = total_candy % people
print(f"Each person gets: {share}")
print(f"leftover candy: {leftover}")


# Part 3: Include the sick friend
# Variable reassignment is fine - previous values were already printed
people += 1
share = total_candy//people
leftover = total_candy % people
print(f"Each person gets: {share}")
print(f"Leftover candy: {leftover}")
