#!/usr/bin/env python3
message = 'Congratulations!!! '
score = float(input("Provide your numeric score"))
# if input value was higher or equal to 90
if score >= 90:
    message = message + "Your associated Grade is A"
elif score >= 80:
    message = message + "Your associated Grade is B"
elif score >= 70:
    message = message + "Your associated Grade is C"
else:
    message = message + "Your associated Grade is D"
print(message)
