# =========================
# Array24
# Arifmetik progressiya bo‘lsa ayirmani, aks holda 0
# =========================
n = int(input())
a = list(map(int, input().split()))

d = a[1] - a[0]
ok = True

for i in range(2, n):
    if a[i] - a[i - 1] != d:
        ok = False
        break

print(d if ok else 0)


# =========================
# Array25
# Geometrik progressiya bo‘lsa maxrajni, aks holda 0
# =========================
n = int(input())
a = list(map(int, input().split()))

if a[0] == 0:
    print(0)
else:
    q = a[1] / a[0]
    ok = True

    for i in range(2, n):
        if a[i - 1] == 0 or a[i] / a[i - 1] != q:
            ok = False
            break

    print(q if ok else 0)
    
    # =========================
# Array26
# Juft/toq ketma-ketligi tekshirish
# =========================
n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(1, n):
    if a[i] % 2 == a[i - 1] % 2:
        ans = i
        break

print(ans)

# =========================
# Array27
# Musbat/manfiy ketma-ketligi
# =========================
n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(1, n):
    if (a[i] > 0 and a[i - 1] > 0) or (a[i] < 0 and a[i - 1] < 0):
        ans = i
        break

print(ans)
# =========================
# Array28
# Juft indekslar minimumi
# =========================
n = int(input())
a = list(map(int, input().split()))

mn = a[0]

for i in range(0, n, 2):
    mn = min(mn, a[i])

print(mn)
# =========================
# Array29
# Toq indekslar maksimumi
# =========================
n = int(input())
a = list(map(int, input().split()))

mx = a[1]

for i in range(1, n, 2):
    mx = max(mx, a[i])

print(mx)
# =========================
# Array30
# O‘ng qo‘shnisidan katta elementlar
# =========================
n = int(input())
a = list(map(int, input().split()))

res = []

for i in range(n - 1):
    if a[i] > a[i + 1]:
        res.append(i)

print(len(res))
print(*res)
# =========================
# Array31
# Chap qo‘shnisidan katta elementlar
# =========================
n = int(input())
a = list(map(int, input().split()))

res = []

for i in range(n - 1, 0, -1):
    if a[i] > a[i - 1]:
        res.append(i)

print(len(res))
print(*res)
# =========================
# Array32
# Birinchi lokal minimum indeksi
# =========================
n = int(input())
a = list(map(int, input().split()))

for i in range(1, n - 1):
    if a[i] < a[i - 1] and a[i] < a[i + 1]:
        print(i)
        break
    # =========================
# Array33
# Oxirgi lokal maksimum indeksi
# =========================
n = int(input())
a = list(map(int, input().split()))

for i in range(n - 2, 0, -1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        print(i)
        break
    # =========================
# Array34
# Lokal minimumlar ichida kattasi
# =========================
n = int(input())
a = list(map(int, input().split()))

mins = []

for i in range(1, n - 1):
    if a[i] < a[i - 1] and a[i] < a[i + 1]:
        mins.append(a[i])

print(max(mins))
    # =========================
# Array35
# Lokal maksimumlar ichida kichigi
# =========================
n = int(input())
a = list(map(int, input().split()))

mxs = []

for i in range(1, n - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        mxs.append(a[i])

print(min(mxs))

# =========================
# Array36
# Lokal min/max bo‘lmaganlar ichida kattasi
# =========================
n = int(input())
a = list(map(int, input().split()))

res = []

for i in range(1, n - 1):
    local_min = a[i] < a[i - 1] and a[i] < a[i + 1]
    local_max = a[i] > a[i - 1] and a[i] > a[i + 1]

    if not local_min and not local_max:
        res.append(a[i])

print(max(res) if res else 0)
# =========================
# Array37
# Monoton o‘suvchi oraliqlar soni
# =========================
n = int(input())
a = list(map(int, input().split()))

cnt = 0
i = 0

while i < n - 1:
    if a[i] < a[i + 1]:
        cnt += 1
        while i < n - 1 and a[i] < a[i + 1]:
            i += 1
    else:
        i += 1

print(cnt)
# =========================
# Array38
# Monoton kamayuvchi oraliqlar soni
# =========================
n = int(input())
a = list(map(int, input().split()))

cnt = 0
i = 0

while i < n - 1:
    if a[i] > a[i + 1]:
        cnt += 1
        while i < n - 1 and a[i] > a[i + 1]:
            i += 1
    else:
        i += 1

print(cnt)
# =========================
# Array39
# Monoton oraliqlar soni
# =========================
n = int(input())
a = list(map(int, input().split()))

cnt = 0
i = 0

while i < n - 1:
    if a[i] < a[i + 1]:
        cnt += 1
        while i < n - 1 and a[i] < a[i + 1]:
            i += 1

    elif a[i] > a[i + 1]:
        cnt += 1
        while i < n - 1 and a[i] > a[i + 1]:
            i += 1
    else:
        i += 1

print(cnt)
# =========================
# Array40
# R ga eng yaqin element
# =========================
n = int(input())
a = list(map(int, input().split()))
R = int(input())

best = a[0]

for x in a:
    if abs(x - R) < abs(best - R):
        best = x

print(best)
# =========================
# Array41
# Yig‘indisi eng katta 2 qo‘shni element
# =========================
n = int(input())
a = list(map(int, input().split()))

mx = a[0] + a[1]
idx = 0

for i in range(1, n - 1):
    s = a[i] + a[i + 1]
    if s > mx:
        mx = s
        idx = i

print(a[idx], a[idx + 1])
# =========================
# Array42
# Yig‘indisi R ga eng yaqin 2 qo‘shni element
# =========================
n = int(input())
a = list(map(int, input().split()))
R = int(input())

best_sum = a[0] + a[1]
idx = 0

for i in range(1, n - 1):
    s = a[i] + a[i + 1]

    if abs(s - R) < abs(best_sum - R):
        best_sum = s
        idx = i

print(a[idx], a[idx + 1])