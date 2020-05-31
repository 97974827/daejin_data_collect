

# # from pythonping import ping
import os
# import pin
res = os.system("timeout 1 ping -c 1 192.168.0.223")
res1 = os.system("timeout 1 ping -c 1 192.168.0.7")
print(res)
print(res1)
# # res1 = ping("192.168.0.7", count=1, timeout=1)
# print(res)
# # print("res1", res1)
#
# if res == "Request timed out":
#     print("실패")
    


# os.system("ping")