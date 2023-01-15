import instaloader
insta = instaloader.Instaloader()
dp = input("Enter username : ")
insta.download_profile(dp, profile_pic_only=True)
print("Profile Picture of",dp,"downloaded sucessfully😄")