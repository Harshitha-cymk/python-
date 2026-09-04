import random

print("======================================")
print("          SECURE OTP SYSTEM")
print("======================================")

name = input("Enter your name: ")
mobile = input("Enter your mobile number: ")

otp = random.randint(100000, 999999)

print("\nOTP has been generated successfully.")
print("Hello", name + "!")
print("Your OTP is:", otp)

attempt = int(input("\nEnter the OTP received: "))

if attempt == otp:
    print("\n✅ OTP VERIFIED SUCCESSFULLY!")
    print("Welcome,", name)
else:
    print("\n❌ INVALID OTP!")
    print("Verification failed.")

print("======================================")
print("          THANK YOU")
print("======================================")
