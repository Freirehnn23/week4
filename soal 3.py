celcius_to_fahrenheit = lambda c: (9/5) * c + 32

celcius_to_reamur = lambda c: 0.8 * c

input_celsius_1 = 100
input_celsius_2 = 80
input_celsius_3 = 0

output_fahrenheit = celcius_to_fahrenheit(input_celsius_1)
output_reamur = celcius_to_reamur(input_celsius_2)

print(f"Input C = {input_celsius_1}. Output F = {output_fahrenheit}.")
print(f"Input C = {input_celsius_2}. Output R = {output_reamur}.")

print(f"Input = {input_celsius_3}. Output F = {celcius_to_fahrenheit(input_celsius_3)}.")
