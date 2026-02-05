---
## 一、Streamlit 顯示圖片（class4-1）

### 🌟 今天學到什麼？

我們學會用 **Streamlit** 把圖片顯示在網頁上！
---

### 🖼️ 顯示一張圖片

```python
st.image("image/apple.png", width=300, caption="蘋果")
```

意思是：

- 顯示一張圖片
- `width`：圖片寬度
- `caption`：圖片下面的說明文字

---

### 📂 一次顯示資料夾裡所有圖片

```python
image_files = os.listdir("image")
```

這行是在做什麼？

- 去 `image` 資料夾
- 把裡面所有檔案名字拿出來

接著用 `for` 迴圈：

```python
for image_file in image_files:
    st.image("image/" + image_file)
```

👉 就可以 **一張一張把圖片全部顯示出來**

---

## 二、簡單購物平台（class4-2）

### 🛒 我們做了什麼？

做了一個 **可以買東西的購物網站** 😆

有：

- 商品圖片
- 價格
- 庫存
- 購買按鈕
- 新增庫存

---

### 🧠 新學到的重要東西

#### 1️⃣ `st.session_state`

👉 用來「記住資料」，不會因為重新整理就不見

例如：

```python
ss = st.session_state
```

裡面放：

- 商品名字
- 價格
- 庫存
- 圖片路徑

---

#### 2️⃣ 欄位排版（columns）

```python
cols = st.columns(3)
```

意思是：

- 把畫面分成 3 欄
- 商品可以排得整整齊齊

---

#### 3️⃣ 購買商品

```python
if st.button("購買"):
    stock -= 1
```

👉 按下按鈕
👉 庫存減 1
👉 沒庫存就不能買

---

#### 4️⃣ 新增庫存

```python
ss.product[name]["stock"] += add_stock
```

意思是：

- 幫商品補貨
- 庫存數量變多

---

## 三、什麼是「函數」（class4-3）

### 🤔 函數是什麼？

👉 **把一段常用的程式碼包起來**
👉 要用的時候直接叫它

就像：

- 洗衣機（丟衣服 → 自動洗好）

---

### ✋ 最簡單的函數

```python
def hello():
    print("hello")
```

使用：

```python
hello()
```

👉 每叫一次，就說一次 hello

---

### 📦 有參數的函數

```python
def greet(name):
    print("Hello", name)
```

使用：

```python
greet("Alice")
```

👉 把名字丟進去，函數幫你說話

---

### 🔢 回傳答案（return）

```python
def two_num_min(a, b):
    return a if a < b else b
```

👉 函數幫你算
👉 把答案「拿回來用」

---

### 🟡 有預設值的參數

```python
def circle_area(r, pi=3.14):
```

意思是：

- 如果沒有給 `pi`
- 就用 3.14

---

## 四、全域變數 & 區域變數（class4-4）

### 🧠 重要觀念（超重要‼️）

---

### 🌍 全域變數

```python
length = 5
```

👉 全世界（整個程式）都看得到

---

### 🏠 區域變數

```python
def test():
    area = 25
```

👉 只在函數裡用
👉 函數外面看不到

---

### ❌ 常見錯誤

在函數裡改變變數，但外面沒變 😱
因為那是 **區域變數**

---

### ✅ 正確做法 1：用 return

```python
def cal():
    return length * length

area = cal()
```

👉 最安全、最推薦 👍

---

### ⚠️ 正確做法 2：global（不太建議）

```python
def cal():
    global area
    area = length * length
```

👉 會直接改外面的變數
👉 新手容易搞混

---

## 🎯 今天重點總結

✔️ 會用 Streamlit 顯示圖片
✔️ 會用迴圈顯示很多圖片
✔️ 做出簡單購物平台
✔️ 了解什麼是函數
✔️ 知道「全域」和「區域」變數的差別

---
