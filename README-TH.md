# สรุปคำสั่ง Git (ฉบับอ่านง่าย)

เอกสารนี้จัดเรียงคำสั่ง Git ที่คุณให้มาให้อ่านง่ายขึ้น พร้อมคำอธิบายสั้น ๆ และตัวอย่างการใช้งาน

---

## ตั้งค่าข้อมูลผู้ใช้ (Global config)
ก่อนจะเริ่มใช้งาน ควรกำหนดชื่อผู้ใช้และอีเมล เพื่อให้ประวัติการ commit ระบุผู้ทำงานได้ถูกต้อง

- ตั้งชื่อผู้ใช้:
```bash
git config --global user.name "YourGitHubUsername"
```

- ตั้งอีเมล:
```bash
git config --global user.email "you@example.com"
```

- ตรวจสอบตัวช่วยจัดการข้อมูลรับรอง (credential helper):
```bash
git config --global credential.helper
```
ตัวอย่างค่าที่พบบ่อย:
- cache (ชั่วคราว) — git จะจำรหัสในหน่วยความจำชั่วคราว
- store (ไม่ปลอดภัยสำหรับเครื่องร่วม) — เก็บรหัสลงไฟล์ plaintext
- osxkeychain / wincred / manager-core — ตัวจัดการรหัสบนระบบปฏิบัติการ

- ดูค่าทั้งหมดที่ตั้งไว้:
```bash
git config --list
```

---

## เริ่มต้นโปรเจกต์และจัดการไฟล์
- เปิดใช้งาน Git ในโฟลเดอร์โปรเจกต์:
```bash
git init
```

- เพิ่มไฟล์ทั้งหมดเข้าสู่ staging area:
```bash
git add .
```
หมายเหตุ: ถ้าต้องการเพิ่มไฟล์บางไฟล์ ให้ระบุชื่อไฟล์แทน `.`

- สร้าง commit พร้อมข้อความ:
```bash
git commit -m "ข้อความบันทึกสำหรับการเปลี่ยนแปลงนี้"
```

---

## สร้าง/เปลี่ยนชื่อสาขา (branch)
- เปลี่ยนชื่อสาขาปัจจุบันเป็น `main`:
```bash
git branch -M main
```

ถ้าต้องการสร้างสาขาใหม่แล้วสลับไปที่สาขานั้น:
```bash
git switch -c new-branch
# หรือ (เก่า)
git checkout -b new-branch
```

---

## เชื่อมต่อกับรีโมท (เช่น GitHub) และส่งรหัส
- เพิ่ม remote ชื่อ `origin` (ตัวอย่างสำหรับ GitHub):
```bash
git remote add origin https://github.com/your-username/your-repo.git
```

- ตรวจสอบ remote ที่เชื่อมอยู่:
```bash
git remote -v
```

- ส่งโค้ดขึ้นสู่ remote branch `main` ครั้งแรก:
```bash
git push -u origin main
```
ตัวเลือก `-u` จะทำให้ branch ท้องถิ่นจับคู่กับ remote branch และช่วยให้ใช้ `git push` / `git pull` ได้ง่ายขึ้นในครั้งต่อไป

---

## คำสั่งตรวจสอบสถานะและประวัติ
- ดูสถานะไฟล์ (ไฟล์ที่เปลี่ยน / ยังไม่ได้ commit / ยังไม่ถูก add):
```bash
git status
```

- ดูประวัติ commit:
```bash
git log --oneline --graph --decorate --all
```
(แสดงแบบย่อพร้อมแผนผังสาขา)

---

## เคล็ดลับและคำเตือน
- แทนที่ `YourGitHubUsername` และ `you@example.com` ด้วยข้อมูลจริงของคุณ
- ระวังการใช้ `credential.helper store` บนเครื่องที่คนอื่นใช้ร่วม เพราะจะเก็บรหัสเป็น plain text
- ก่อน push ตรวจสอบว่า remote URL ถูกต้องและมีสิทธิ์เขียน (push) บน repo นั้น
- ถ้ารีโมทเป็น SSH ให้ใช้ URL แบบ `git@github.com:owner/repo.git` แทน HTTPS

---

ถ้าต้องการ ผมสามารถ:
- แปลเป็นภาษาอังกฤษ
- ช่วยสร้างไฟล์ README หรือ cheat-sheet ที่สั้นลง
- ช่วยรันคำสั่งหรือ push ให้ (ต้องการสิทธิ์และรายละเอียดเพิ่มเติม)