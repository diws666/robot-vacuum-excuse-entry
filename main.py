import os

EXCUSE = "I was not stuck under the couch for three hours. I was conducting a thorough inspection of the dust situation."  # 110 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(EXCUSE)

print(len(EXCUSE.encode("utf-8")), "bytes")
print(open("/output/entry.txt", "rb").read() == EXCUSE.encode("utf-8"))
